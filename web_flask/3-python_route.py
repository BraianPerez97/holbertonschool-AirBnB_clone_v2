#!/usr/bin/python3
""" Start Flask webapp """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return hello"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Return HBNB"""
    return ('HBNB')


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """returns c variable"""
    return "C " + text.replace('_', " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text="is cool"):
    if text is not "is cool":
        text = text.replace('_', " ")
    return f"Python {text}"


if __name__ == "__main__":
    """runs"""
    app.run(host='0.0.0.0', port='5000')
