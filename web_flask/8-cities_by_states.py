#!/usr/bin/python3
"""
Starts a Flask web application
"""


import os
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ removes current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ displays 8-cities_by_states.html """
    states = storage.all("State").values()
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = []
        for state in states:
            cities.append(state.cities)
    else:
        cities = states.cities()
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
