import os

# adding database
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # adding configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    # adding database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False