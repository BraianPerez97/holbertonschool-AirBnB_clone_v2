#!/usr/bin/python3
from flask import Flask
""" Hello Flask """


app = Flask(__name__)


@app.route('/', strict_slashes=False)
"""Hello HBND"""


def hello_hbnd():
    return "Hello HBND!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
