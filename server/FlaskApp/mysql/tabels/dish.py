from FlaskApp.services.errorHandler import ErrorHandler
TABLE_NAME = 'Dish'
DISH_ING_TABLE = 'Dish_ingredients'

def insert(dish):
    if not validate_dish(dish):
        return False
    query = 'INSERT INTO {table} VALUES(0,"{name}", {calories}, "{recipes}", {peopleCount}, {cookingTime}, "{photoLink}")'.format(
        table=TABLE_NAME,
        name=dish['name'],
        calories=dish['calories'],
        recipes=dish['recipe'],
        peopleCount=dish['peopleCount'],
        cookingTime=dish['cookingTime'],
        photoLink=dish['photoLink'])
    return query


def get_dish_id(dish):
    if not validate_dish(dish):
        return False
    query = 'SELECT id FROM {table} WHERE name="{name}"'.format(table=TABLE_NAME, name=dish['name'])
    return query


def get(dish):
    validate_dish_search(dish)
    query = 'SELECT * FROM {table} WHERE name LIKE "%{name}%"'.format(table=TABLE_NAME,
                                                                      name=dish['text'])
    return query


def get_dish_with_sliders(dish, calories, cookingTime):
    validate_dish_search(dish)
    query = 'SELECT * FROM {table} WHERE name LIKE "%{name}% AND' \
            ' calories <= {calories}" AND cookingTime <= {cookingTime}"'.format(table=TABLE_NAME,
                                                                                name=dish['text'],
                                                                                calories=dish[calories],
                                                                                cookingTime=dish[cookingTime])
    return query


def get_dish_without_ings(ing_ids_lst):
    if ing_ids_lst is None:
        return False  # maybe change to the simple get dish#
    first = True
    query = 'SELECT DISTINCT id FROM {table}'.format(table=DISH_ING_TABLE)
    query += 'EXCEPT ('
    for ing_id in ing_ids_lst:
        if first is False:
            query += ' UNION '
        else:
            first = False
        query += '(SELECT DISTINCT id FROM {table} WHERE ing_id="{ing_id}")'.format(table=DISH_ING_TABLE,
                                                                                    ing_id=ing_id['ing_id'])
    query += ')'
    return query


def full_get_dish(dish, calories, cookingTime, ing_ids_lst):
    query = get_dish_with_sliders(dish,calories, cookingTime)
    if ing_ids_lst is None:
        return query
    query += 'INTERSECT ('
    query += get_dish_without_ings(ing_ids_lst)
    query += ' )'
    return query


def validate_dish_search(dish):
    if 'text' not in dish:
        raise ErrorHandler(403, "validation failed")


def validate_dish(dish):
    if 'name' not in dish:
        return False
    if 'recipe' not in dish:
        return False
    if 'peopleCount' not in dish:
        return False
    if 'cookingTime' not in dish:
        return False
    if 'photoLink' not in dish:
        return False
    if 'calories' not in dish:
        return False
    return True
