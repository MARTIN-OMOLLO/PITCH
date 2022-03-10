from flask import render_template,redirect,url_for
from . import auth
from flask_login import login_user, login_required, logout_user
from .form import LoginForm, RegistrationForm
from ..models import User
from flask_login import login_user
# from ..email import mail_message
from .. import db

# ....
@auth.route('/login',methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit:
        user = User.query.filter_by(email = login_form.email.data,password = login_form.password.data)
        if user is not None and login_form.password == login_form.password.data:
            login_user(user,login_form.remember.data)
            db.session.add(user)
            flash ('Username and Password are invalid')
            return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/login.html',login_form= login_form)


@auth.route('/signup',methods = ["GET","POST"])
def signup():
    signup_form = RegistrationForm()
    if signup_form.validate_on_submit:
        user = User.query.filter_by(email = signup_form.email.data, username = signup_form.username.data,password = signup_form.password.data)
        print("the user instance", user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',registrationform= signup_form)


@auth.route('/logout',methods = ["GET","POST"])
def logout():
    login_form = LoginForm()
    if login_form.validate_on_submit:
        user = User.query.filter_by(email = form.email.data, username = login_form.username.data,password = login_form.password.data)
        logout_user(user,login_form.remember.data)
        return redirect(url_for('auth.login'))
    return render_template('auth/logout.html',log_out= login_form)