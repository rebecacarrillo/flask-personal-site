from flask import Flask, Blueprint, render_template, abort
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/oops')
def oops():
    return render_template('mistakes.html')

@app.route('/next')
def nxt():
    return render_template('next.html')

@app.route('/old')
def old():
    return render_template('old.html')

@app.route('/art')
def art():
    return render_template('art.html')

@app.route('/values')
def values():
    return render_template('values.html')

def create_app():
    with app.app_context():
        Bootstrap(app)
        return app



