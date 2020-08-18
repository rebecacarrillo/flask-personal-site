app = Flask(__name__)
app.config['TESTING'] = False
app.config['FREEZER_BASE_URL'] = 'http://borky.xyz/'