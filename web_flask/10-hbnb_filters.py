#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Render the template '10-hbnb_filters.html' with states and amenities data.

    This route fetches all states and amenities from the database
    and passes them
    to the template for rendering.

    Returns:
        rendered HTML template with states and amenities data.
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
            "10-hbnb_filters.html",
            states=states,
            amenites=amenities)


@app.teardown_appcontext
def teardown(exc):
    """
    Close the database connection after each request.

    This function is called by Flask after each request to
    close the SQLAlchemy session
    and release the database connection resources.

    Args:
        exc (Exception): The exception raised during the request, if any.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
