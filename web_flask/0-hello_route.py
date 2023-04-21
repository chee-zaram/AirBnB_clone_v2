#!/usr/bin/python3
"""This file uses flask to display a given string"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This is the index page"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Control starts here"""
    app.run(host='0.0.0.0', port=5000)
