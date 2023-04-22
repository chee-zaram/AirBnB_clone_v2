#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """Displays a HTML page like 6-index.html"""

    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    amenities = sorted(list(storage.all(Amenity).values()),
                       key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    """Start of the application"""
    app.run(host="0.0.0.0", port=5000)
