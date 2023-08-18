#!/usr/bin/python3
""" Start Flask webapp """
from flask import Flask, render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def int_n(n):
    """print int"""
    if type(n) is int:
        return f"{n} is a number"
    else:
        raise TypeError


@app.route('/number_template/<int:n>', strict_slashes=False)
def html(n):
    """print html"""
    if type(n) is int:
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    """route that evaluates if n is odd or even"""
    if type(n) is int:
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html',
                                   number=n, text='odd')
    else:
        raise TypeError


if __name__ == "__main__":
    """runs"""
    app.run(host='0.0.0.0', port='5000')
