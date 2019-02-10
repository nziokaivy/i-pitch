import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'c2ef723c5c795661596125cc1a8e2fb2'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ivy:New Password@localhost/pitch'    