from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '21ad0163f7774319409a266fcca95b16'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db '

db = SQLAlchemy(app)
migrate = Migrate(app, db)



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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title=title, form=form)    

@app.route('/login', methods=['GET', 'POST'])
def login():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Login'
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
        else:
            flash('Login unsuccessful.Please check username and password!', 'danger')    
        return redirect(url_for('home'))
    return render_template('login.html', title=title, form=form)

if __name__ == '__main__':
    app.run(debug=True)