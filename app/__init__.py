from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLACHEMY(app)

# Initializing application
app = Flask(__name__)

from app import views