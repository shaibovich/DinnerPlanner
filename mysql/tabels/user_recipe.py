from services.errorHandler import ErrorHandler

TABLE_NAME = 'User_recipe'
DISH_TABLE = 'Dish'


def insert(obj):
    validate_insert_obj(obj)
    query = 'INSERT INTO {table} VALUE(%s, %s, %s, %s, %s, %s,%s)'.format(
        table=TABLE_NAME)

    return query, (obj['user'], obj['dish_id'], obj['calories'], obj['recipe'], obj['peopleCount'], obj['cookingTime'],
                   obj['photoLink'])


def get_all_user_recipes(user_id):
    query = 'SELECT {DISH_TABLE}.dish_id, {DISH_TABLE}.name, {DISH_TABLE}.calories, {table}.recipe, {DISH_TABLE}.peopleCount, {DISH_TABLE}.cookingTime, {DISH_TABLE}.photoLink FROM {table}, {DISH_TABLE} WHERE {table}.user_id = %s AND {table}.dish_id = {DISH_TABLE}.dish_id'.format(
        table=TABLE_NAME,
        DISH_TABLE=DISH_TABLE)

    return query, (user_id)


def get_user_recipe(user_id, dish_id):
    query = 'SELECT * FROM {table} WHERE user_id=%s AND dish_id=%s'.format(table=TABLE_NAME)
    return query, (user_id, dish_id)


def update_recipe(obj):
    validate_insert_obj(obj)
    query = 'UPDATE {table} SET calories=%s, recipe=%s, peopleCount=%s, cookingTime=%s, photoLink=%s WHERE dish_id=%s AND user_id=%s'.format(
        table=TABLE_NAME)
    return query, (
        obj['calories'], obj['recipe'], obj['peopleCount'], obj['cookingTime'], obj['photoLink'], obj['dish_id'],
        obj['user'])


def delete_user_recipe(user_id, dish_id):
    query = 'DELETE FROM {table} WHERE dish_id=%s AND user_id=%s'.format(table=TABLE_NAME)
    return query, (dish_id, user_id)


def validate_insert_obj(obj):
    if 'user' not in obj:
        raise ErrorHandler(403, "Dish : validation failed, no user")
    if 'dish_id' not in obj:
        raise ErrorHandler(403, "Dish : validation failed, no dish id")
    if 'calories' not in obj:
        raise ErrorHandler(403, "Dish : validation failed, no calories")
    if 'recipe' not in obj:
        raise ErrorHandler(403, "Dish : validation failed, no recipe")
    if 'peopleCount' not in obj:
        raise ErrorHandler(403, "Dish : validation failed, no peopleCount")
    if 'cookingTime' not in obj:
        raise ErrorHandler(403, "Dish : validation failed, no cookingTime")
    if 'photoLink' not in obj:
        raise ErrorHandler(403, "Dish : validation failed, no photoLink")
