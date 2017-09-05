#!/usr/bin/python3
"""
Starts a Flask web application
"""


from flask import Flask
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
    return 'C %s' % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ displays Python followed by value of text variable """
    text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
