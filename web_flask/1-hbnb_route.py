#!/usr/bin/python3
"""This is a file to start a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello():
    """
    This function return a string when a request is made to /hbnb
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
