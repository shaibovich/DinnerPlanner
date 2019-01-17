from FlaskApp.services.errorHandler import ErrorHandler
import datetime

TABLE_NAME = 'User_meals'


def insert(user_id, name):
    creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if not validate_insert(user_id, creation_date):
        return None
    query = 'INSERT INTO {table} VALUES( {user_id}, 0, "{name}",  "{creation_date}")'.format(table=TABLE_NAME,
                                                                                           user_id=user_id,
                                                                                           name=name,
                                                                                           creation_date=creation_date)
    return query


def validate_insert(user_id, creation_date):
    if user_id is None or creation_date is None:
        raise ErrorHandler(403, "validation error insert")
    return isinstance(user_id, int)


def validate_get(user_id):
    if user_id is None:
        raise ErrorHandler(403, "validation error get")
    return isinstance(user_id, int)


def get(user_id):
    validate_get(user_id)
    query = 'SELECT * FROM {table} WHERE user_id="{user_id}"'.format(table=TABLE_NAME,
                                                                     user_id=user_id)
    return query


def exists(user_id, meal_id):
    query = 'SELECT COUNT(*) as count FROM {table} WHERE user_id="{user_id}" AND meal_id="{meal_id}"'.format(
        table=TABLE_NAME,
        user_id=user_id,
        meal_id=meal_id)
    return query


def remove_meal(user_id, meal_id):
    query = 'DELETE FROM {table} WHERE(meal_id="{meal_id}" AND user_id="{user_id}")'.format(table=TABLE_NAME,
                                                                                            meal_id=meal_id,
                                                                                            user_id=user_id)
    return query
