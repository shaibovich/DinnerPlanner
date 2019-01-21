from services.errorHandler import ErrorHandler


def validate_request(request):
    if not request.is_json:
        raise ErrorHandler(403, "Validation failed : No Data")
    if request.json is None:
        raise ErrorHandler(403, "Validation failed : No Data")


def validate_get_request(request, params):
    if request is None:
        raise ErrorHandler(403, "Validation failed : No params")
    if request.args is None:
        raise ErrorHandler(403, "Validation failed : No params")
    for param in params:
        if request.args.get(param) is None:
            raise ErrorHandler(403, "Validation failed ,  no param : {}".format(param))
