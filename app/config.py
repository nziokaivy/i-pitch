import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'c2ef723c5c795661596125cc1a8e2fb2'