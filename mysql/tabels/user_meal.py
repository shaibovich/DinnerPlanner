from services.errorHandler import ErrorHandler
import datetime

TABLE_NAME = 'User_meals'


def insert(user_id, name):
    creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    validate_insert(user_id, creation_date)
    query = 'INSERT INTO {table} VALUES( %s, 0, %s,  %s)'.format(table=TABLE_NAME)
    return query, (user_id, name, creation_date)


def validate_insert(user_id, creation_date):
    if user_id is None or creation_date is None:
        raise ErrorHandler(403, "User Meal : validation failed, no user id")


def validate_get(user_id):
    if user_id is None:
        raise ErrorHandler(403, "User Meal : validation failed, no user id")


def get(user_id):
    validate_get(user_id)
    query = 'SELECT * FROM {table} WHERE user_id=%s'.format(table=TABLE_NAME)
    return query, (user_id)


def remove_meal(user_id, meal_id):
    query = 'DELETE FROM {table} WHERE meal_id=%s AND user_id=%s'.format(table=TABLE_NAME)
    return query, (meal_id, user_id)
