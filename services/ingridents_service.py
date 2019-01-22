from services.abstract_service import abstrac_service
from mysql.tabels.ingridents import insert, get_all, exists, insert_many, get_by_dish_id, get_by_name


class ingridents_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)

    def add_ingrident(self, ing):
        self.validate_and_convert_ing(ing)
        query, params = insert(ing)
        id = self.db.insert(query, params)
        ing['id'] = id
        return self.return_success(ing)

    def add_ingridents(self, ing_list):
        new_insert_list = []
        for ing in ing_list:
            self.validate_and_convert_ing(ing_list[ing])
            query, params = exists(ing_list[ing])
            if self.db.is_exists(query, params) is False:
                new_insert_list.append(ing_list[ing])
        if len(new_insert_list) == 0:
            return None
        query, params = insert_many(new_insert_list)
        res = self.db.insert(query, params)
        if res:
            return self.return_success(new_insert_list)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def get_all_ingridents(self):
        query, params = get_all()
        result = self.db.get(query, params)
        return self.return_success(self.ingredients_response(result))

    def get_all_dish_ingerients(self, dish_id):
        query, params = get_by_dish_id(dish_id)
        result = self.db.get(query, params)
        return self.convert_dish_ingerdient_to_list(result)

    def search_ing(self, name):
        query, params = get_by_name(name)
        result = self.convert_ing(self.db.get(query, params))
        return self.return_success(result)

    def convert_ing(self, result):
        lst = []
        for res in result:
            lst.append({
                'id': res[0],
                'name': res[1]
            })

        return lst

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
