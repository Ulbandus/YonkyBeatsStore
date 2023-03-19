from app import app
from flask import render_template, redirect, send_file
#from .tools import Store


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/beats')
def beats():
    return render_template('beats.html', current_page='beats')


@app.route('/faq')
def faq():
    return render_template('faq.html', current_page='faq')


@app.route('/login')
def login():
    return render_template('beats.html')


@app.route('/admin')
def admin():
    return render_template('beats.html')


@app.route('/favicon.ico')
def favicon():
    return send_file('static/images/favicon.ico')


@app.errorhandler(404)
def error(error):
    return redirect('/')
