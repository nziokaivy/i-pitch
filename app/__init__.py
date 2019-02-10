from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 

engine = create_engine('sqlite:///site.db', echo=True)
Base = declarative_base()
import os
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2ef723c5c795661596125cc1a8e2fb2'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
login_manager =LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

Base.metadata.create_all(engine)

from app import views