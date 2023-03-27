from flask import Flask
from .config import database_dir

app = Flask(__name__, template_folder='./templates/')

from app import routes
