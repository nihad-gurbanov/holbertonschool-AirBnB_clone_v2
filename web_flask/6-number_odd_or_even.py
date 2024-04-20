#!/usr/bin/python3

"""
HelloHBNB Flask Application
"""

from flask import Flask
from flask import render_template


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


# @app.route('/c', strict_slashes=False)
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):
    """
    Route that accepts an optional parameter with default value.

    Args:
        text (str): Text to be included in the response.

    Returns:
        str: A message containing the provided text.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def n(n):
    """
    Route to display if the provided parameter is an integer.

    Args:
        n (int): The parameter passed to the route.

    Returns:
        str: A message indicating whether the parameter is an integer or not.
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def render(n):
    """
    Renders an HTML template with a dynamic value if n is int.

    Args:
        n (str): The value to be displayed in the template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('5-number.html', n=str(n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_n(n):
    """
    Renders an HTML template with a dynamic value if n is int odd | even.

    Args:
        n (str): The value to be displayed in the template.

    Returns:
        str: Rendered HTML template.
    """
    if n % 2 == 0:
        result = f'{n} is even'
    else:
        result = f'{n} is odd'
    return render_template('6-number_odd_or_even.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
