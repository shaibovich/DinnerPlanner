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
                                                 dish_id=dish)
        if index == len(dish_list) - 1:
            query += ';'
        else:
            query += ','
    return query

def delete_all_meal_dishes(meal_id):
    query = 'DELETE FROM {table} WHERE meal_id={meal_id}'.format(table=TABLE_NAME,
                                                                 meal_id=meal_id)
    return query


def validate_insert(meal_id, dish_id, creation_date):
    if dish_id is None or meal_id is None or creation_date is None:
        raise ErrorHandler(403, "validation error")


def validate_get(meal_id):
    if meal_id is None:
        raise ErrorHandler(403, "validation error")


def get_dishes(meal_id):
    validate_get(meal_id)
    query = 'SELECT Dish.dish_id,  Dish.name, Dish.calories, Dish.recipe, Dish.peopleCount, Dish.cookingTime, Dish.photoLink FROM {table}, Dish  WHERE {table}.meal_id={meal_id} AND {table}.dish_id = Dish.dish_id '.format(table=TABLE_NAME,
                                                                     meal_id=meal_id)
    return query

def add_edited_dishes(user_id, query):
    query = '(' + query + 'AND Dish.dish_id '
    query += 'NOT IN (SELECT dish_id FROM User_recipe WHERE user_id={user_id}))'.format(user_id=user_id)
    query += ' UNION '
    query += '(SELECT Dish.dish_id, Dish.name, User_recipe.calories, User_recipe.recipe, User_recipe.peopleCount, User_recipe.cookingTime, User_recipe.photoLink FROM User_recipe, Dish WHERE user_id={user_id} AND Dish.dish_id = User_recipe.dish_id)'.format(user_id=user_id)
    return query

# (SELECT Dish.dish_id,  Dish.name, Dish.calories, Dish.recipe, Dish.peopleCount, Dish.cookingTime, Dish.photoLink
#  FROM Meal_dishes, Dish
#  WHERE Meal_dishes.meal_id=15
#    AND Meal_dishes.dish_id = Dish.dish_id
#    AND Dish.dish_id NOT IN
#        (SELECT dish_id
#         FROM User_recipe
#         WHERE user_id=2))
# UNION
#     (SELECT User_recipe.dish_id, Dish.name, User_recipe.calories, User_recipe.recipe, User_recipe.peopleCount, User_recipe.cookingTime, User_recipe.photoLink
#       FROM User_recipe, Dish
#       WHERE user_id=2
#         AND User_recipe.dish_id = Dish.dish_id)




def remove_dish_from_meal(meal_id, dish_id):
    if not validate_insert(meal_id, dish_id):
        return None
    query = 'DELETE FROM {table} WHERE(meal_id = {meal_id} AND dish_id = {dish_id})'.format(table=TABLE_NAME,
                                                                                            meal_id=meal_id,
                                                                                            dish_id=dish_id)
    return query
