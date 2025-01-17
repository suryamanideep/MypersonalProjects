from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

# import pyodbc

app = Flask(__name__)
app.secret_key = "this is tuff"
app.config['TESTING'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contactapp.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('Email_User')
app.config['MAIL_PASSWORD'] = os.environ.get('Email_Password')
app.config['MAIL_SUPPRESS_SEND'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'Login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from contactapp import routes
