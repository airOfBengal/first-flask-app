from flask import Flask, render_template, request
from forms import LoginForm

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


users = {"atiq@email.com": "atiq", "rony@email.com": "rony"}


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
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template(
                    "login.html", form=form, message="Successfully Logged In"
                )
        return render_template(
            "login.html", form=form, message="Incorrect Email or Password"
        )
    elif form.errors:
        print(form.errors.items())

    return render_template("login.html", form=form)


@app.route("/about")
def about():
    return 'We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology "adopt, don\'t hop"! '


@app.route("/<my_name>")
def greetings(my_name):
    return "Welcome " + my_name + "!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
