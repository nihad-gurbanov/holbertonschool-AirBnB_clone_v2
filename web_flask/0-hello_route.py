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
    return 'HelloHBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
