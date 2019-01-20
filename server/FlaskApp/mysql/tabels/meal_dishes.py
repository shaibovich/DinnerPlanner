from FlaskApp.services.errorHandler import ErrorHandler
import datetime

TABLE_NAME = 'Meal_dishes'


def insert(meal_id, dish_id):
    creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    validate_insert(meal_id, dish_id, creation_date)
    query = 'INSERT INTO {table} VALUES(%s, %s, %s)'.format(table=TABLE_NAME)
    return query, (meal_id, dish_id, creation_date)


def insert_many(meal_id, dish_list):
    query = 'INSERT INTO {table} (meal_id, dish_id) VALUES '.format(table=TABLE_NAME)
    values = ()
    for index, dish in enumerate(dish_list):
        query += '(%s, %s)'
        values += (meal_id, dish)
        if index == len(dish_list) - 1:
            query += ';'
        else:
            query += ','
    return query, values


def delete_all_meal_dishes(meal_id):
    query = 'DELETE FROM {table} WHERE meal_id=%s'.format(table=TABLE_NAME)

    return query, (meal_id)


def validate_insert(meal_id, dish_id, creation_date):
    if dish_id is None or meal_id is None or creation_date is None:
        raise ErrorHandler(403, "validation error")


def validate_get(meal_id):
    if meal_id is None:
        raise ErrorHandler(403, "validation error")


def get_dishes(meal_id):
    validate_get(meal_id)
    query = 'SELECT Dish.dish_id,  Dish.name, Dish.calories, Dish.recipe, Dish.peopleCount, Dish.cookingTime, Dish.photoLink FROM {table}, Dish  WHERE {table}.meal_id=%s AND {table}.dish_id = Dish.dish_id '.format(
        table=TABLE_NAME)
    return query, (meal_id)


def add_edited_dishes(user_id, query):
    query = '(' + query + 'AND Dish.dish_id '
    query += 'NOT IN (SELECT dish_id FROM User_recipe WHERE user_id={user_id}))'.format(user_id=user_id)
    query += ' UNION '
    query += '(SELECT Dish.dish_id, Dish.name, User_recipe.calories, User_recipe.recipe, User_recipe.peopleCount, User_recipe.cookingTime, User_recipe.photoLink FROM User_recipe, Dish WHERE user_id={user_id} AND Dish.dish_id = User_recipe.dish_id)'.format(
        user_id=user_id)
    return query


def remove_dish_from_meal(meal_id, dish_id):
    if not validate_insert(meal_id, dish_id, None):
        return None
    query = 'DELETE FROM {table} WHERE(meal_id = %s AND dish_id = %s)'.format(table=TABLE_NAME)

    return query, (meal_id, dish_id)
