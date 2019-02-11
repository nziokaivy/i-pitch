import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db, mail
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from ..email import send_email



@auth.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    title = 'Register'
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User( username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to i-pitch","email/welcome_user",user.email,user=user)
        flash(f'Account created for {form.username.data}! You are now able to log in', 'success')
        
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='New Account', form=form)
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    title = 'Login'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password:
            login_user(user, remember=form.remember.data)
            next_page = requests.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:    
            flash('Login unsuccessful.Please check email and password!', 'danger')    
        return redirect(url_for('home'))
    return render_template('auth/login.html', title=title, form=form)


@auth.route('/logout')
@loginrequired
def logout():
    logout_user()
    return redirect(ulr_for('home'))
