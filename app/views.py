from flask import Flask, render_template, url_for
from app import app
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY']

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

@app.route('/register')
def register():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Register'
    form = RegistrationForm()
    return render_template('register.html', title=title, form=form)    

@app.route('/login')
def login():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Login'
    form = LoginForm()
    return render_template('login.html', title=title, form=form)    