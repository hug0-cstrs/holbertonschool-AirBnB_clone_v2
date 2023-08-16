#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/states')
def states():
    states = storage.all("State")
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def states_given_id(id):
    states = storage.all("State")
    found_state = ""
    for s_id in states:
        if s_id == id:
            found_state = states[s_id]

    return render_template('9-states.html',
                           state=found_state)


@app.teardown_appcontext
def teardown(err):
    """remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
