from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)


def create_app():
    with app.app_context():
        from . import routes  # Import routes
        Bootstrap(app)
        return app



