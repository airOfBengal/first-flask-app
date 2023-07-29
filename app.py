from flask import Flask, render_template, request
from forms import LoginForm, SignUpForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "dfewfew123213rwdsgert34tgfd1234trgf"

"""Information regarding the Pets in the System."""
pets = [
    {
        "id": 1,
        "name": "Nelly",
        "age": "5 weeks",
        "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles.",
    },
    {
        "id": 2,
        "name": "Yuki",
        "age": "8 months",
        "bio": "I am a handsome gentle-cat. I like to dress up in bow ties.",
    },
    {
        "id": 3,
        "name": "Basker",
        "age": "1 year",
        "bio": "I love barking. But, I love my friends more.",
    },
    {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."},
]


users = [
    {
        "id": 1,
        "full_name": "Pet Rescue Team",
        "email": "team@pawsrescue.co",
        "password": "adminpass",
    },
]


@app.route("/")
def index():
    return "hello world!"


@app.route("/home")
def home():
    return render_template("home.html", pets=pets)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        for user in users:
            if (
                user["email"] == form.email.data
                and user["password"] == form.password.data
            ):
                return render_template("login.html", message="Successfully Logged In")
        return render_template(
            "login.html", form=form, message="Incorrect Email or Password"
        )
    elif form.errors:
        print(form.errors.items())

    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {
            "id": len(users) + 1,
            "full_name": form.full_name.data,
            "email": form.email.data,
            "password": form.password.data,
        }
        users.append(new_user)
        return render_template("signup.html", message="Successfully signed up")
    return render_template("signup.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/<my_name>")
def greetings(my_name):
    return "Welcome " + my_name + "!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
