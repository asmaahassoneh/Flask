from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "Home Page"


@main.route("/hello/")
def hello():
    return "Hello World!!"
