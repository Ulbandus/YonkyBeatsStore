from app import app
from flask import render_template, redirect, send_file, request


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/beats')
def beats():
    return render_template('beats.html', current_page='beats')


@app.route('/faq')
def faq():
    return render_template('faq.html', current_page='faq')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    # place username and password in settings file
    if username == 'admin' and password == 'admin':
        return render_template('login.html', logged=True, beats=[])
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


from flask_sqlalchemy import SQLAlchemy


with app.app_context():
    database = SQLAlchemy(app)

    class Item(database.Model):
            id = database.Column(database.Integer, primary_key=True)
            title = database.Column(database.String, nullable=False)
            price = database.Column(database.Integer, nullable=False)
            is_sold = database.Column(database.Boolean, default=False)
            tags = database.Column(database.String, nullable=True)
            license_type = database.Column(database.String, nullable=False)
            badges = database.Column(database.String, nullable=True)
            preview = database.Column(database.String, nullable=True)
            bpm = database.Column(database.String, nullable=True)
            tonality = database.Column(database.String, nullable=True)
            genre = database.Column(database.String, nullable=True)
            mood = database.Column(database.String, nullable=True)
    database.create_all()
