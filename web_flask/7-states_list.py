#!/usr/bin/python3
"""It is a script starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/state_list", strict_slashes=False)
def state_list():
    """
    Renders a list of states.

    Returns:
        str: Rendered HTML template.
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


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
