import os

basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import dotenv_values

config = dotenv_values(".flaskenv")

class Config:
    ENV = os.getenv("FLASK_ENV")
    DEBUG = ENV == "development"
    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_PORT = os.getenv("FLASK_PORT")
    DEV = os.getenv("DEV")
    
    # URLs
    
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        # or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
