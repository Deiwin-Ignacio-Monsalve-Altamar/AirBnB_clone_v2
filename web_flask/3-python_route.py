#!/usr/bin/python3
"""/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the
text variable (replace underscore _ symbols with a space )
The default value of text is “is cool"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """starts a Flask web hello_world"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnh():
    """starts a Flask web page /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text='is cool'):
    """ followed by the value of the text python"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
