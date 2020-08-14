app = Flask(__name__)
app.config['TESTING'] = False
app.config['FLASK_ENV'] = 'production'