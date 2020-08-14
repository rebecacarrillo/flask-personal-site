from bapp import app
from flask import Flask, render_template


@app.route('/')
def index():
    return render_template('base.html')
@app.route('/home1')
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

@app.route('/values')
def values():
    return render_template('values.html')

@app.route('/art')
def art():
    return render_template('art.html')

if __name__ == '__main__':
    app.run()