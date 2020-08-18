from flask import Flask, Blueprint, render_template, abort
from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages



app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True




@app.route("/<path:path>.html")
def page(path=None):
    # Look for the page with FlatPages, or find "index" if we have no path
    page = pages.get_or_404(path or 'index')

    # Render the template "page.html" with our page and title
    return render_template("home.html", page=page, title=page.meta['title'])

pages = FlatPages(app)

Bootstrap(app)






@app.route('/')
def index():
    return render_template('base.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/oops.html')
def oops():
    return render_template('mistakes.html')

@app.route('/next.html')
def nxt():
    return render_template('next.html')

@app.route('/old.html')
def old():
    return render_template('old.html')

@app.route('/art.html')
def art():
    return render_template('art.html')

@app.route('/values.html')
def values():
    return render_template('values.html')

def create_app():
    with app.app_context():
        return app



