from flask import Flask, jsonify
from flask_cors import CORS
from logzero import logger


app = Flask(__name__, instance_relative_config=True)

# Setup cors headers to allow all domains
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)


# Definition of the routes. Put them into their own file. See also
# Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
@app.route("/")
def hello_world():
    logger.info("/")
    return "Hello World"


@app.route("/foo/<someId>")
def foo_url_arg(someId):
    logger.info("/foo/%s", someId)
    return jsonify({"echo": someId})


app.config.from_object('config')
