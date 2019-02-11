from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from flask_login import LoginManager
from config import config_options

engine = create_engine('sqlite:///site.db', echo=True)
Base = declarative_base()
import os


# def create_app(config_name):

app = Flask(__name__)

# app.config.from_object(config_options[config_name])

SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
login_manager =LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

Base.metadata.create_all(engine)

from app import views