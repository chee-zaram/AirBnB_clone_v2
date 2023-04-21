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


if __name__ == "__main__":
    """Start of control"""
    app.run(host='0.0.0.0', port=5000)
