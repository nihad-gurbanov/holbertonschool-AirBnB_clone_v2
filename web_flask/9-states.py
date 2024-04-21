#!/usr/bin/python3
"""It is a script starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
    Renders a list of states | by ids.

    Returns:
        str: Rendered HTML template.
    """
    depo = storage.all(State)

    if not id:
        return render_template("7-states_list.html", depo=depo.values())
    
    key = f'State.{id}'
    state = None
    
    try:
        state = depo[key]
    except KeyError:
        pass
    return render_template("9-states.html", state=state)


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
