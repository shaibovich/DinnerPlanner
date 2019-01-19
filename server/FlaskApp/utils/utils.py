# This file will be the util file for the server
from FlaskApp.services.errorHandler import ErrorHandler


def validate_user(user):
    # here we need to validate the user data
    print(user)
    return 1


def validate_request(request):
    if not request.is_json:
        raise ErrorHandler(403, "no object supply")
    if request.json is None:
        raise ErrorHandler(403, "no object supply")


def validate_get_request(request, params):
    if request is None:
        raise ErrorHandler(403, "no param ")
    if request.args is None:
        raise ErrorHandler(403, "no param ")
    for param in params:
        if request.args.get(param) is None:
            raise ErrorHandler(403, "no param : {}".format(param))
