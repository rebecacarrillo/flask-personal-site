from flask import Flask, Blueprint, render_template, abort
from flask_bootstrap import Bootstrap
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates',
                        static_folder='static')


@simple_page.route('/', defaults={'page': 'home'})
@simple_page.route('/<page>')
#@simple_page.route('/about', )

def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


app = Flask(__name__)
app.register_blueprint(simple_page)


def create_app():
    with app.app_context():
        from . import routes  # Import routes
        Bootstrap(app)
        return app



