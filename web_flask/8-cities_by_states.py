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
    states_all = storage.all("State").values()
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        states = {}
        for state in states_all:
            states['id'] = state.id
            states['name'] = state.name
            for city in state.cities:
                cities = {}
                if city.state_id == state.id:
                    cities['id'] = city.id
                    cities['name'] = city.name
            if len(cities) > 0:
                states['cities'] = cities
        print(states)
    else:
        cities = states.cities()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
