from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class SignUpForm(FlaskForm):
    full_name = StringField("Full Name:")
    email = StringField("Email:", validators=[InputRequired(), Email()])
    password = PasswordField("Password:", validators=[InputRequired(), Length(min=4)])
    confirm_password = PasswordField(
        "Confirm Password:",
        validators=[InputRequired(), Length(min=4), EqualTo("password")],
    )
    submit = SubmitField("Sign UP")
