from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2ef723c5c795661596125cc1a8e2fb2'
app.config['SQLACHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ivy:password/pitch'

SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


from app import views