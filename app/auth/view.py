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
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)