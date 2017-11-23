from flask import Flask, Blueprint
from flask_cors import CORS

from pywally.api import api
from pywally.api.views.sessions import ns as sessions_ns

app = Flask(__name__, instance_relative_config=True)

# Setup cors headers to allow all domains
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)

app.config.from_object('config')


@app.route('/')
def index():
    """Sample HTTP route"""
    return 'Hello, world!'


def initialize():
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(sessions_ns)
    # NS config goes here
    app.register_blueprint(blueprint)
