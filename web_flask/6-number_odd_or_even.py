#!/usr/bin/python3
""" Start Flask webapp """
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Return hello"""
    return ("Hello HBNB!")


@app.route("/hbnb")
def hello_hbnb():
    """Return HBNB"""
    return ('HBNB')


@app.route("/c/<text>")
def c_fun(text):
    """returns c variable"""
    return "C " + text.replace('_', " ")


@app.route('/python/')
@app.route('/python/<text>')
def python_cool(text="is cool"):
    if text is not "is cool":
        text = text.replace('_', " ")
    return f"Python {text}"


@app.route('/number/<int:n>')
def int_n(n):
    """print int"""
    if type(n) is int:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """print html"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def is_odd_or_even(n):
    """route that evaluates if n is odd or even"""
    if type(n) is int:
        if n % 2 == 0:
            return render_template('6-number_odd_or_even.html', n=n)
    else:
        raise TypeError


if __name__ == "__main__":
    """runs"""
    app.run(host='0.0.0.0', port='5000')
