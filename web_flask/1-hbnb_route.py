#!/bin/usr/python3
"""starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    """starts a Flask web application"""
    return 'Hello, HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """starts a Flask web application"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
