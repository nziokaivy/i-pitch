from flask import render_template, url_for, flash, redirect
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user


posts = [
    {
        'author' : 'Ivy Mwende',
        'title' : 'Pitch 1 content',
        'content' : 'Beautiful day in Kenya',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'John Doe',
        'title' : 'Pitch 2 content',
        'content' : 'Beautiful day in Uganda',
        'date_posted' : 'April 21, 2018'

    }
]

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/home')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    return render_template('home.html', title=title, posts=posts)    

@app.route('/register', methods=['GET', 'POST'])
def register():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Register'
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User( username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data}! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title=title, form=form)    

@app.route('/login', methods=['GET', 'POST'])
def login():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Login'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and pass_secure.check_password_hash(user.password, form.password.data)
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:    
            flash('Login unsuccessful.Please check email and password!', 'danger')    
        return redirect(url_for('home'))
    return render_template('login.html', title=title, form=form)

