from app import app
from flask import render_template, redirect, send_file, request
from .config import config
from .tools import Store


@app.route('/')
def home():
    return render_template('home.html', beats=store.get_all())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == config['SETTINGS']['username'] and\
           password == config['SETTINGS']['password']:
            return render_template('login.html', logged=True,
                                   beats=store.get_all())
    return render_template('login.html', logged=False)


@app.route('/admin')
def admin():
    return render_template('beats.html')


@app.route('/favicon.ico')
def favicon():
    return send_file('static/images/favicon.ico')


@app.errorhandler(404)
def error(error):
    return redirect('/')


@app.route('/temp')
def temp():
    return render_template('temp.html')


store = Store()
