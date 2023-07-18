#!/usr/bin/python3
"""
Script that starts a Flask web application to list states and individual states
"""

from flask import Flask, render_template
from models import storage

# create a Flask instance
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display a HTML page with a list of all states."""
    from models.state import State
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_cities_by_states(id):
    """Display a HTML page with the state list by id integer"""
    from models.state import State
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
