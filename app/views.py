from flask import Flask, render_template, url_for
from app import app

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

