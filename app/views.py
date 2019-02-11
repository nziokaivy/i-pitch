from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    return render_template('login.html', title=title, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(ulr_for('home'))

@app.route('/account')
@login_required
def account():
    form = UpdateAccountForm()
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    
    return render_template('account.html', title='Account', image_file=image_file, form=form)