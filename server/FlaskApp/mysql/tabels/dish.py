from FlaskApp.services.errorHandler import ErrorHandler
TABLE_NAME = 'Dish'


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
    query = 'SELECT * FROM {table} WHERE name="{name}"'.format(table=TABLE_NAME,
                                                               name=dish['text'])
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
