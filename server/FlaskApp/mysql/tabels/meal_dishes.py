import datetime

TABLE_NAME = 'meal_dishes'


def insert(meal_id, dish_id):
    creation_date = datetime.date.now()
    if not validate_insert(meal_id, dish_id, creation_date):
        return None
    query = 'INSERT INTO {table} VALUES({meal_id}, {dish_id}, {creation_date})'.format(table=TABLE_NAME,
                                                                                       meal_id=meal_id,
                                                                                       dish_id=dish_id,
                                                                                       creation_date=creation_date)
    return query


def validate_insert(meal_id, dish_id, creation_date):
    if dish_id is None or meal_id is None or creation_date is None:
        return False
    return isinstance(dish_id, int) and isinstance(meal_id, int) and isinstance(creation_date, datetime)


def validate_get(meal_id):
    if meal_id is None:
        return False
    return isinstance(meal_id, int)


def get(meal_id):
    validate_get(meal_id)
    query = 'SELECT * FROM {table} WHERE meal_id="{meal_id}"'.format(table=TABLE_NAME,
                                                                     meal_id=meal_id)
    return query


def remove_dish_from_meal(meal_id, dish_id):
    if not validate_insert(meal_id, dish_id):
        return None
    query = 'DELETE FROM {table} WHERE(meal_id = {meal_id} AND dish_id = {dish_id})'.format(table=TABLE_NAME,
                                                                                            meal_id=meal_id,
                                                                                            dish_id=dish_id)
    return query
