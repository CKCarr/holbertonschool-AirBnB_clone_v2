#!/usr/bin/python3
"""This is a file to start a Flask web application"""
from flask import Flask, render_template


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


@app.route('/python', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """ This function return a string when a request
    is made to /python/<text> """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ This function return a string when a request
    is made to /number/<n> """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ display a HTML page only if n is an integer -
        determine in template if number is even or odd
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
