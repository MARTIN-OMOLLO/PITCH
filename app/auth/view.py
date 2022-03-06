from flask import render_template,redirect,url_for
from ..models import auth
from flask_login import login_user, login_required, logout_user
from .forms import LoginForm, RegistrationForm
from ..models import User
from flask_login import login_user
from ..email import mail_message
from .. import db

# ....
@auth.route('/login',methods = ["GET","POST"])
def login():
    form = LoginForm():
        if form.validate_on_submit:
        user = User.query.filter_by(email = form.email.data, username = form.username.data,password = form.password.data)
        if user != none and user.verify_password(form.password.data)
        login_user(user,form.remember.data)
        db.session.add(user)
        flash ('Username and Password are invalid')
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/login.html',loginform= form)


    @auth.route('/signup',methods = ["GET","POST"])
def signup():
    form = RegisterForm():
        if form.validate_on_submit:
        user = User.query.filter_by(email = form.email.data, username = form.username.data,password = form.password.data)
        print("the user instance", user)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html',reg_form= form)


    @auth.route('/logout',methods = ["GET","POST"])
def logout():
    form = LoginForm():
        if form.validate_on_submit:
        user = User.query.filter_by(email = form.email.data, username = form.username.data,password = form.password.data)
        logout_user(user,form.remember.data)
        return redirect(url_for('auth.login'))
    return render_template('auth/logout.html',log_out= form)