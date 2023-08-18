#!/usr/bin/python3
""" Start Flask webapp """
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display "HBNB" when accessing the '/hbnb' route"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Display "C " followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is_cool"):
    """Display "Python " followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def is_number(n):
    """Display "<n> is a number" when accessing the
    '/number/<n>' route"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Display an HTML page with a header tag displaying
    "Number: n" """
    if isinstance(n, int):
        return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Display an HTML page with a header tag displaying
    "Number: n is even|odd" """
    if isinstance(n, int):
        even_or_odd = "odd" if n % 2 != 0 else "even"
        return render_template('6-number_odd_or_even.html',
                               number=n, even_or_odd=even_or_odd)


if __name__ == "__main__":
    """runs"""
    app.run(host='0.0.0.0', port='5000')
