#!/usr/bin/python3

"""
HelloHBNB Flask Application
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Root route of the application.

    Returns:
        str: A simple greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Sample url of the application.

    Returns:
        str: A simple message.
    """
    return 'HBNB'


@app.route('/c', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Route that accepts an optional parameter.

    Args:
        text (str): Text to be included in the response.

    Returns:
        str: A message containing the provided text.
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
