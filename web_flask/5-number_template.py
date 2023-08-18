#!/usr/bin/python3
""" Start Flask webapp """
from flask import Flask, render_template, escape
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
    return "C {}".format(escape(text).replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_cool(text="is cool"):
    return "Python {}".format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>')
def int_n(n):
    """print int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_temp(n):
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    """runs"""
    app.run(host='0.0.0.0', port='5000')
