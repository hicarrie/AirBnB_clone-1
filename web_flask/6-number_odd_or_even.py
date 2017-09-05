#!/usr/bin/python3
"""
Starts a Flask web application
"""


from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ displays Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB! """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ displays C followed by value of text variable """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ displays Python followed by value of text variable """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ displays n is a number only if n is an integer """
    try:
        return '{} is a number'.format(int(n))
    except:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """ displays n is a number only if n is an integer """
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """ displays n if it is a number and if it is even or odd """
    try:
        n = int(n)
        return render_template('6-number_odd_or_even.html', n=n)
    except:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
