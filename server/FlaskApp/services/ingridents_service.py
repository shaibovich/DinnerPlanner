from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels.ingridents import insert, get_all, exists, insert_many, get_by_dish_id


class ingridents_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)

    def add_ingrident(self, ing):
        obj = self.validate_and_convert_ing(ing)
        if obj is None:
            return self.return_validation_err("Ing is invalid : {}".format(ing))
        query = insert(ing)
        if self.db.insert(query):
            return self.return_success(ing)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def add_ingridents(self, ing_list):
        new_insert_list = []
        for ing in ing_list:
            self.validate_and_convert_ing(ing_list[ing])
            query = exists(ing_list[ing])
            if self.db.is_exists(query) is False:
                new_insert_list.append(ing_list[ing])
        if len(new_insert_list) == 0:
            return None
        query = insert_many(new_insert_list)
        res = self.db.insert(query)
        if res:
            return self.return_success(new_insert_list)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def get_all_ingridents(self):
        query = get_all()
        result = self.db.get(query)
        return self.return_success(self.ingredients_response(result))

    def get_all_dish_ingerients(self, dish_id):
        query = get_by_dish_id(dish_id)
        result = self.db.get(query)
        return self.convert_dish_ingerdient_to_list(result)

    def convert_dish_ingerdient_to_list(self, result):
        lst = []
        for res in result:
            lst.append({
                'id': res[0],
                'name': res[1],
                'count': res[2]
            })
        return lst

    def validate_and_convert_ing(self, ing):
        if 'name' not in ing:
            self.return_validation_err("ing not valid")


    def ingredients_response(self, result_lst):
        list = []
        for res in result_lst:
            list.append({
                'id': res[0],
                'name': res[1]
            })
        return list
