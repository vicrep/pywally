from flask import Blueprint, jsonify
from logzero import logger

sample_page = Blueprint('simple_page', __name__)


# Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
@sample_page.route("/")
def hello_world():
    logger.info("/")
    return "Hello World"


@sample_page.route("/foo/<someId>")
def foo_url_arg(someId):
    logger.info("/foo/%s", someId)
    return jsonify({"echo": someId})
