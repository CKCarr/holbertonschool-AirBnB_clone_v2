#!/usr/bin/python3
"""This is a file to start a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """This function return a string when a request is made to root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function return a string when a request is made to /hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_C(text):
    """
    This function return a string when a request is made to /c/<text>
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text='is cool'):
    """ This function return a string when a request
    is made to /python/<text> """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
