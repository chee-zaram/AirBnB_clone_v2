#!/usr/bin/python3
"""A flask practice application"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display a string for the number route"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Renders a html file if `n` is an int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Renders a html page depending on whether integer `n` is odd or even"""
    odd = False
    if n % 2 != 0:
        odd = True
    return render_template('6-number_odd_or_even.html', n=n, odd=odd)


if __name__ == "__main__":
    """Start of control"""
    app.run(host='0.0.0.0', port=5000)
