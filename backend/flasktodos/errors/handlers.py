import traceback

from flask import Blueprint, current_app
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException


blueprint = Blueprint("error_handlers", __name__)


# Send JSON instead of HTML when HTTP exceptions are raised.
@blueprint.app_errorhandler(HTTPException)
def http_error_handler(e):
    return {"message": e.description}, e.code


# Send HTTP 422 response when request data is not valid.
@blueprint.app_errorhandler(ValidationError)
def validation_error_handler(e):
    return {"errors": e.messages}, 422


# Send JSON instead of HTML when Python exceptions are raised.
@blueprint.app_errorhandler(Exception)
def server_error_handler(e):
    if isinstance(e, (HTTPException, ValidationError)):
        return e

    current_app.logger.exception(e)

    response = {"message": "Internal Server Error"}

    if current_app.debug:
        response["error"] = str(e)
        response["stack"] = traceback.format_exception(e)

    return response, 500
