#!/usr/bin/python3
"""It is a script starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Renders a list of cities by states.

    Returns:
        str: Rendered HTML template.
    """
    depo = storage.all(State).values()
    return render_template("8-cities_by_states.html", depo=depo)


@app.teardown_appcontext
def teardown(exc):
    """
    Closes the storage after each request or application context.

    Args:
        exc (Exception): The exception object if an exception occurred
        during the request handling.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
