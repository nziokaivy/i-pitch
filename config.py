import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'c2ef723c5c795661596125cc1a8e2fb2'

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")    
    
class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}    