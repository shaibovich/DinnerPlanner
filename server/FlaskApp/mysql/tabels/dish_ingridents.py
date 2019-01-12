TABLE_NAME = 'dish_ingrident'


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
        query += '({ing_id}, {dish_id}, {amount})'.format(ing_id=ing_list[ing]['id'],
                                                          dish_id=dish_id,
                                                          amount=2)
        if index == len(ing_list) - 1:
            query += ';'
        else:
            query += ','
    return query


def validate_onj(dish_id, ing_id, amount):
    if dish_id is None or ing_id is None or amount is None:
        return False
    return isinstance(dish_id, int) and isinstance(ing_id, int) and isinstance(amount, int) and amount > 0
