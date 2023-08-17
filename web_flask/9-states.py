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


@app.route('/states/<id>', strict_slashes=False)
def cities_of_state(id):
    """Get cities by states"""
    list_states = storage.all(State)
    for state in list_states.values():
        if state.id == id:
            cities = state.cities
            return render_template('9-states.html', states=list_states,
                                   cities=cities, state=state,
                                   current_route="route_cities")
    return render_template('9-states.html', current_route="not found")


@app.teardown_appcontext
def teardown(err):
    """remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
