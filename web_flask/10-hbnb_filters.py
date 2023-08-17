#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    all_info = {}
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    for state in states:
        all_info[state.name] = state

    return render_template('10-hbnb_filters.html',
                           states=all_info,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(err):
    """remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
