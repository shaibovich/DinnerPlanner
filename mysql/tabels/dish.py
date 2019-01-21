from services.errorHandler import ErrorHandler

TABLE_NAME = 'Dish'
DISH_ING_TABLE = 'Dish_ingredients'


def insert(dish):
    validate_dish(dish)
    query = 'INSERT INTO {table} VALUES(0, %s, %s, %s, %s, %s, %s)'.format(
        table=TABLE_NAME)
    return query, (
        dish['name'], dish['calories'], dish['recipe'], dish['peopleCount'], dish['cookingTime'], dish['photoLink'])


def get_dish_id(dish):
    validate_dish(dish)
    query = 'SELECT id FROM {table} WHERE name=%s'.format(table=TABLE_NAME)
    return query, (dish['name'])


def get(dish):
    validate_dish_search(dish)
    query = 'SELECT * FROM {table} WHERE name LIKE "%s%"'.format(table=TABLE_NAME)
    return query, (dish['text'])


def get_dish_with_sliders(dish):
    validate_dish_search(dish)
    query = 'SELECT * FROM {table} WHERE name LIKE "%{name}%" '.format(table=TABLE_NAME,
                                                                       name=dish['text'])

    return query


def get_dish_with_ings(ing_ids_lst):
    query = 'AND dish_id IN (SELECT DISTINCT dish_id FROM {DISH_TABLE} WHERE '.format(DISH_TABLE=DISH_ING_TABLE)
    for index, ing in enumerate(ing_ids_lst):
        query += 'ing_id={ing_id}'.format(ing_id=ing)
        if index == len(ing_ids_lst) - 1:
            query += ')'
        else:
            query += ' AND '
    return query


def get_dish_without_ing(ing_ids_lst):
    query = 'AND dish_id NOT IN (SELECT DISTINCT dish_id FROM {DISH_TABLE} WHERE '.format(DISH_TABLE=DISH_ING_TABLE)
    for index, ing in enumerate(ing_ids_lst):
        query += 'ing_id={ing_id}'.format(ing_id=ing)
        if index == len(ing_ids_lst) - 1:
            query += ')'
        else:
            query += ' AND '
    return query


def get_dish_with_calories_range(min_calories, max_calories):
    if max_calories == '' and min_calories == '':
        return ''
    min_query = ''
    max_query = ''
    if min_calories != '' and min_calories > 0:
        min_query = ' AND calories >= {min} '.format(min=min_calories)
    if max_calories != '' and max_calories > 0:
        max_query = ' AND calories <= {max} '.format(max=max_calories)
    return min_query + max_query


def get_dish_with_cooking_time_range(min_cooking, max_cooking):
    if min_cooking == '' and max_cooking == '':
        return ''
    min_query = ''
    max_query = ''
    if min_cooking != '' and min_cooking > 0:
        min_query = ' AND cookingTime >= {min} '.format(min=min_cooking)
    if max_cooking != '' and max_cooking > 0:
        max_query = ' AND cookingTime <= {max} '.format(max=max_cooking)
    return min_query + max_query


def full_get_dish(dish, calories, cookingTime, with_ing_ids_lst, without_ing_ids_lst):
    query = get_dish_with_sliders(dish)
    query += get_dish_with_cooking_time_range(cookingTime['min'], cookingTime['max'])
    query += get_dish_with_calories_range(calories['min'], calories['max'])

    if with_ing_ids_lst is not None and isinstance(with_ing_ids_lst, list) and len(with_ing_ids_lst) != 0:
        query += get_dish_with_ings(with_ing_ids_lst)

    if without_ing_ids_lst is not None and isinstance(without_ing_ids_lst, list) and len(without_ing_ids_lst) != 0:
        query += get_dish_without_ing(without_ing_ids_lst)

    return query


def validate_dish_search(dish):
    if 'text' not in dish:
        raise ErrorHandler(403, "Dish search : validation failed, no text")


def validate_dish(dish):
    if 'name' not in dish:
        raise ErrorHandler(403, "Dish : validation failed, no name")
    if 'recipe' not in dish:
        raise ErrorHandler(403, "Dish : validation failed, no recipe")
    if 'peopleCount' not in dish:
        raise ErrorHandler(403, "Dish : validation failed, no peopleCount")
    if 'cookingTime' not in dish:
        raise ErrorHandler(403, "Dish : validation failed, no cookingTime")
    if 'photoLink' not in dish:
        raise ErrorHandler(403, "Dish : validation failed, no photoLink")
    if 'calories' not in dish:
        raise ErrorHandler(403, "Dish : validation failed, no calories")
