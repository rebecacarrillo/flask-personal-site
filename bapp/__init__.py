from flask import Flask


app = Flask(__name__)

def create_app():
    """Construct the core application."""

    init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        return app