from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
# For configuration
app.config.from_object(Config)
# For data base
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Create Flask-Login
login = LoginManager(app)
# Force to login before viewing certain pages
login.login_view = 'login'

from app import routes, models, errors

