from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2ef723c5c795661596125cc1a8e2fb2'
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///site.db '
db = SQLAlchemy(app)


from app import views