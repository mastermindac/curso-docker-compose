import traceback

from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException

from .app import app


# Send JSON instead of HTML when HTTP exceptions are raised.
@app.errorhandler(HTTPException)
def http_error_handler(e):
    return {"message": e.description}, e.code


# Send HTTP 422 response when request data is not valid.
@app.errorhandler(ValidationError)
def validation_error_handler(e):
    return {"errors": e.messages}, 422


# Send JSON instead of HTML when Python Exceptions are raised.
@app.errorhandler(Exception)
def server_error_handler(e):
    if isinstance(e, (HTTPException, ValidationError)):
        return e

    traceback.print_exception(e)

    response = {"message": "Internal Server Error"}

    if app.debug:
        response["error"] = str(e)
        response["stack"] = traceback.format_exc()

    return response, 500
