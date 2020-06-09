from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User, Category
from .forms import SignUpForm, LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required
from ..email import mail_message

# app.config['SECRET_KEY'] =''
@auth.route('/signup', methods = ["GET", "POST"])
def signup():
    form = SignUpForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Pitch","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    title = "New Account | Pitch"
    return render_template('auth/signup.html', signup_form = form, title=title, categories=categories)

@auth.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password', 'danger')
    
    title = "Login | Pitch"
    return render_template('auth/login.html', login_form = form, title=title, categories=categories)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))