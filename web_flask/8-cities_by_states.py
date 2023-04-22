#!/usr/bin/python3
"""Start a web application for HBNB"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_route():
    """Displays the a html page"""
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', states=all_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Renders a page which displays cities by states"""
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def tear_down(error):
    """Ends the database session"""
    storage.close()


if __name__ == "__main__":
    """Start of the application"""
    app.run(host='0.0.0.0', port=5000)
