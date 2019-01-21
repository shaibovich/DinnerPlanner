from services.errorHandler import ErrorHandler

TABLE_NAME = 'User'


def get(user):
    validate_get(user)
    query = 'SELECT * FROM {table} WHERE email=%s AND password=%s'.format(table=TABLE_NAME)
    return query, (user['email'], user['password'])


def insert(user):
    validate_insert(user)

    obj = {
        'email': user['email'],
        'password': user['password'],
        'name': user['user']
    }

    query = "INSERT INTO {table} VALUES(0,%s ,%s,%s )".format(table=TABLE_NAME)

    return query, (obj['email'], obj['password'], obj['name'])


def validate_get(user):
    if 'email' not in user:
        raise ErrorHandler(403, "User : Validation failed, no email")
    if 'password' not in user:
        raise ErrorHandler(403, "User : Validation failed, no password")


def validate_insert(user):
    validate_get(user)
    if 'user' not in user:
        raise ErrorHandler(403, "User : Validation failed, no user")
