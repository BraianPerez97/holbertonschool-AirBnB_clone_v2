#!/usr/bin/python3
# import Flask class from flask module
from flask import Flask

# Create an instance of Flask class and assing it to var 'app'
app = Flask(__name__)

# Define root URL ('/') ans disable stric_slashes


@app.route('/', strict_slashes=False)
def hello_hbnd():
    # Function is executed when access to URL
    return "Hello HBND!"


if __name__ == "__main__":
    # Run flask app, making it listen to 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
