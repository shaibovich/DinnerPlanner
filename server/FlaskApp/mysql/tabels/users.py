TABLE_NAME = 'Users'
from werkzeug.security import generate_password_hash, check_password_hash


def get(user):
    validate_get(user)
    query = 'SELECT * FROM {table} WHERE email="{email}" AND password="{password}"'.format(table=TABLE_NAME,
                                                                                           email=user['email'],
                                                                                           # password=generate_password_hash(user['password'], salt_length=2))
                                                                                           password=user['password'])
    return query


def insert(user):
    if validate_insert(user):
        print("validation error for user : {user}".format(user=user))
        return None
    else:
        obj = {
            'email': user['email'],
            # 'password': generate_password_hash(user['password'], salt_length=2),
            'password': user['password'],
            'name': user['user']
        }
        query = "INSERT INTO {table} VALUES('{email}','{name}','{password}')".format(table=TABLE_NAME,
                                                                                     email=obj['email'],
                                                                                     password=obj['password'],
                                                                                     name=obj['name'])
        return query


def validate_get(user):
    if 'email' not in user:
        return False
    if 'password' not in user:
        return False
    return True


def validate_insert(user):
    if validate_get(user):
        return False
    if 'user' not in user:
        return False
    return True
