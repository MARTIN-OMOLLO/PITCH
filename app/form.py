from flask_wtf import FlaskForm
from wtforms import ValidateionError, StringField,Password,SubmitField,BooleanField
from wtforms,validators import Required,Email, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    Remember = BooleanField('Remember Me')
    Submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required()])