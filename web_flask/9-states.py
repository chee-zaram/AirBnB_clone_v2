#!/usr/bin/python3
"""Starts a web application for HBNB"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=""):
    """Displays all states or a state with a given id"""

    states = storage.all(State).values()

    if not id:
        return render_template('9-states.html', states=states, lone_state=None)

    for st in states:
        if st.id == id:
            return render_template('9-states.html', states=None, lone_state=st)
    return render_template('9-states.html', states=None, lone_state=None)


@app.teardown_appcontext
def tear_down(error):
    """Ends the database session"""
    storage.close()


if __name__ == "__main__":
    """Start of the application"""
    app.run(host='0.0.0.0', port=5000)
