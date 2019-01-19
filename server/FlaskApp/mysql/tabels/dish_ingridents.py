from FlaskApp.services.errorHandler import ErrorHandler
from FlaskApp.mysql.tabels.dish import get_dish_id, get

TABLE_NAME = 'Dish_ingredients'
MEAL_DISHES_TABLE = 'Meal_dishes'
ING_TABLE = 'Ingredients'


def insert(dish_id, ing_id, amount):
    if not validate_onj(dish_id, ing_id, amount):
        return None
    query = 'INSERT INTO {table} VALUES({ing_id}, {dish_id}, {amount})'.format(table=TABLE_NAME,
                                                                               dish_id=dish_id,
                                                                               ing_id=ing_id,
                                                                               amount=amount)
    return query


def insert_many(dish_id, ing_list):
    query = 'INSERT INTO {table} (ing_id, dish_id, amount) VALUES '.format(table=TABLE_NAME)
    for index, ing in enumerate(ing_list):
        query += '({ing_id}, {dish_id}, {amount})'.format(ing_id=ing['id'],
                                                          dish_id=dish_id,
                                                          amount=ing['count'])
        if index == len(ing_list) - 1:
            query += ';'
        else:
            query += ','
    return query


def validate_onj(dish_id, ing_id, amount):
    if dish_id is None or ing_id is None or amount is None:
        return False
    return isinstance(dish_id, int) and isinstance(ing_id, int) and isinstance(amount, int) and amount > 0


def get_dish_with_ing(dish, ing_id):
    if ing_id is None:
        return False
    query = 'SELECT DISTINCT id FROM {table} WHERE ing_id="{ing_id}"'.format(table=TABLE_NAME,
                                                                             ing_id=ing_id['ing_id'])
    return query


# TODO check if needed##
def get_dish_without_ing(ing_id):
    if ing_id is None:
        return False
    query = 'SELECT DISTINCT id FROM {table} ' \
            'EXCEPT' \
            'SELECT DISTINCT id FROM {table} WHERE ing_id="{ing_id}"'.format(table=TABLE_NAME,
                                                                             ing_id=ing_id['ing_id'])
    return query


def get_dish_without_ings(ing_ids_lst):
    if ing_ids_lst is None:
        return False  # maybe change to the simple get dish#
    first = True
    query = 'SELECT DISTINCT id FROM {table}'.format(table=TABLE_NAME)
    query += 'EXCEPT ('
    for ing_id in ing_ids_lst:
        if first is False:
            query += ' UNION '
        else:
            first = False
        query += '(SELECT DISTINCT id FROM {table} WHERE ing_id="{ing_id}")'.format(table=TABLE_NAME,
                                                                                    ing_id=ing_id['ing_id'])
    query += ')'
    return query


def get_dish_without_ingsV2(ing_ids_lst):
    if ing_ids_lst is None:
        return False  # maybe change to the simple get dish#
    query = 'SELECT DISTINCT id FROM {table}'.format(table=TABLE_NAME)
    for ing_id in ing_ids_lst:
        query += 'EXCEPT SELECT DISTINCT id FROM {table} WHERE ing_id="{ing_id}"'.format(table=TABLE_NAME,
                                                                                         ing_id=ing_id['ing_id'])
    return query


def meal_ingredients(meal_id):
    query = 'SELECT {Meal_dish}.meal_id, {table}.ing_id, SUM({table}.amount) as num, {ing}.name ' \
            'FROM {table}, {Meal_dish}, {ing} WHERE {Meal_dish}.meal_id = {meal_id} ' \
            'AND {Meal_dish}.dish_id = {table}.dish_id ' \
            'AND {ing}.ing_id = {table}.ing_id ' \
            'GROUP BY {ing}.ing_id ' \
            'ORDER BY {ing}.name'.format(table=TABLE_NAME,
                                         ing=ING_TABLE,
                                         Meal_dish=MEAL_DISHES_TABLE,
                                         meal_id=meal_id)
    return query
