#!/usr/bin/python3
"""Starts Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Display list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    """Runs"""
    app.run(host='0.0.0.0', port=5000)
