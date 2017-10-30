from flask import Flask
from flask_cors import CORS

from pywally.blueprints.sample_page import sample_page

app = Flask(__name__, instance_relative_config=True)

# Setup cors headers to allow all domains
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)


# Definition of the routes. Put them into their own file.
app.register_blueprint(sample_page)

app.config.from_object('config')
