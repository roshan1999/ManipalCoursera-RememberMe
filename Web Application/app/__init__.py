from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'init_w'
app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)


from app import routes,models,DES
