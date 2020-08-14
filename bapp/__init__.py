from flask import Flask


app = Flask(__name__)

def create_app():
    """Construct the core application."""


    with app.app_context():
        from . import routes  # Import routes

        return app