import datetime


TABLE_NAME = 'user_meal'


def insert(user_id,meal_id):
    creation_date = datetime.date.now()
    if not validate_insert(user_id, meal_id, creation_date):
        return None
    query = 'INSERT INTO {table} VALUES( {user_id}, {meal_id}, {creation_date})'.format(table=TABLE_NAME,
                                                                                        user_id=user_id,
                                                                                        meal_id=meal_id,
                                                                                        creation_date=creation_date)
    return query


def validate_insert(user_id, meal_id, creation_date):
    if user_id is None or meal_id is None or creation_date is None:
        return False
    return isinstance(user_id, int) and isinstance(meal_id, int) and isinstance(creation_date, datetime)


def validate_get(user_id):
    if user_id is None:
        return False
    return isinstance(user_id, int)


def get(user_id):
    validate_get(user_id)
    query = 'SELECT * FROM {table} WHERE user_id="{user_id}"'.format(table=TABLE_NAME,
                                                                     user_id=user_id)
    return query


def exists(user_id, meal_id):
    query = 'SELECT COUNT(*) as count FROM {table} WHERE user_id="{user_id}" AND meal_id="{meal_id}"'.format(table=TABLE_NAME,
                                                                                                             user_id=user_id,
                                                                                                             meal_id=meal_id)
    return query


def remove_meal(user_id, meal_id):
    if not exists(user_id, meal_id):
        return None
    query = 'DELETE FROM {table} WHERE(meal_id="{meal_id}" AND user_id="{user_id}")'.format(table=TABLE_NAME,
                                                                                            meal_id=meal_id,
                                                                                            user_id=user_id)
    return query
