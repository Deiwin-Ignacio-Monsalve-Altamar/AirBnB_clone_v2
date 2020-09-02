#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """reload close files storage"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():

    for place in storage.all(Amenity).values():
        if i == 4:
            break
        print(place)
        i = i + 1
    conntext = {
        'states': storage.all(State).values(),
        'cities': storage.all(City).values(),
        'amenities': storage.all(Amenity).values()
    }
    return render_template('10-hbnb_filters.html', **conntext)


@app.route('/cities_by_states')
def cities_list():
    '''list all states and cities'''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        states = storage.all(State).values()
    else:
        states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
