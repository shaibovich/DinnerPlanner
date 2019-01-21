from services.errorHandler import ErrorHandler

TABLE_NAME = 'Dish_ingredients'
MEAL_DISHES_TABLE = 'Meal_dishes'
ING_TABLE = 'Ingredients'


def insert(dish_id, ing_id, amount):
    validate_onj(dish_id, ing_id, amount)
    query = 'INSERT INTO {table} VALUES(%s, %s, %s)'.format(table=TABLE_NAME)
    return query, (ing_id, dish_id, amount)


def insert_many(dish_id, ing_list):
    query = 'INSERT INTO {table} (ing_id, dish_id, amount) VALUES '.format(table=TABLE_NAME)
    values = ()
    for index, ing in enumerate(ing_list):
        query += '(%s, %s, %s)'
        values += (ing['id'], dish_id, ing['count'])
        if index == len(ing_list) - 1:
            query += ';'
        else:
            query += ','
    return query, values


def validate_onj(dish_id, ing_id, amount):
    if dish_id is None or ing_id is None or amount is None:
        raise ErrorHandler(403,
                           "Dish Ingredient : validation failed, must fill : dish_id(int) , ing_id(int) and amount(int)")
    if isinstance(dish_id, int) and isinstance(ing_id, int) and isinstance(amount, int) and amount > 0:
        return
    else:
        raise ErrorHandler(403,
                           "Dish Ingredient : validation failed, must fill : dish_id(int) , ing_id(int) and amount(int)")


def meal_ingredients(meal_id):
    query = 'SELECT {Meal_dish}.meal_id, {table}.ing_id, SUM({table}.amount) as num, {ing}.name ' \
            'FROM {table}, {Meal_dish}, {ing} WHERE {Meal_dish}.meal_id = %s ' \
            'AND {Meal_dish}.dish_id = {table}.dish_id ' \
            'AND {ing}.ing_id = {table}.ing_id ' \
            'GROUP BY {ing}.ing_id ' \
            'ORDER BY {ing}.name'.format(table=TABLE_NAME,
                                         ing=ING_TABLE,
                                         Meal_dish=MEAL_DISHES_TABLE)

    return query, (meal_id)
