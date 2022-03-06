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
    username = StringField('Enter Your username', validators =[Required()])
    password = PasswordField('Password', validators[Required()])
    password_confirm PasswordField('Cofirm Password', validators = [Required()])
    Submit = SubmitField('Sign Up')

def validate_email(self,data_field):
    if user.query.filter_by(email = data_field.data).first():
        raise ValidateionError("Email Exists.")


def validate_username(self, data_field):
    if User.query.filter_by(username = data_field.data).first()
    raise ValidateionError("Username exists.")