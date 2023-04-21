#!/usr/bin/python3
"""A flask practice application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Root of the url"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Sends hbnb response"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays the string 'C <text>'"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Displays a string for the python route"""
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    """Start of control"""
    app.run(host='0.0.0.0', port=5000)
