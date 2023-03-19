from flask import Flask


app = Flask(__name__, template_folder='./templates/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'


from app import routes

