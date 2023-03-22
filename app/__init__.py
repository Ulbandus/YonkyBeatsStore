from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import database_dir
from .tools import Store

app = Flask(__name__, template_folder='./templates/')
app.config['SQLALCHEMY_DATABASE_URI'] = database_dir

from app import routes

database = SQLAlchemy()
database.init_app(app)

#store = Store(database)
#store.init_tables()
#store.create_tables()
