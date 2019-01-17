from FlaskApp.services.errorHandler import ErrorHandler
import datetime

TABLE_NAME = 'Meal_dishes'


def insert(meal_id, dish_id):
    creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    validate_insert(meal_id, dish_id, creation_date)
    query = 'INSERT INTO {table} VALUES({meal_id}, {dish_id}, "{creation_date}")'.format(table=TABLE_NAME,
                                                                                         meal_id=meal_id,
                                                                                         dish_id=dish_id,
                                                                                         creation_date=creation_date)
    return query


def insert_many(meal_id, dish_list):
    query = 'INSERT INTO {table} (meal_id, dish_id) VALUES '.format(table=TABLE_NAME)
    for index, dish in enumerate(dish_list):
        query += '({meal_id}, {dish_id})'.format(meal_id=meal_id,
                                                 dish_id=dish_list[dish]['id'])
        if index == len(dish_list) - 1:
            query += ';'
        else:
            query += ','
    return query


def validate_insert(meal_id, dish_id, creation_date):
    if dish_id is None or meal_id is None or creation_date is None:
        raise ErrorHandler(403, "validation error")


def validate_get(meal_id):
    if meal_id is None:
        raise ErrorHandler(403, "validation error")


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
