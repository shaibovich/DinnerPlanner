from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels.dish import insert, get_dish_id, get
from FlaskApp.mysql.tabels import dish_ingridents
from FlaskApp.services.ingridents_service import ingridents_service as ingridents_services


class dish_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)
        self.ing_service = ingridents_services(my_sql)

    def add_dish(self, dish):
        # response = self.ing_service.add_ingridents(dish['ingredients'])
        # if response.status_code == 200:
        query = insert(dish)
        if query and self.db.insert(query):
            # here we need to add all the ing to meal
            my_dish = self.db.get(get_dish_id(dish))[0][0]
            if len(list(dish['ingredients'])):
                query = dish_ingridents.insert_many(my_dish, dish['ingredients'])
                if self.db.insert(query):
                    return self.return_success(dish)
                else:
                    return self.return_internal_err("db error for query : {}".format(query))

            return self.return_success(dish)
        else:
            return self.return_internal_err("db error fro query : {}".format(query))

    def search_dish(self, dish):
        query = get(dish)
        if query:
            result = self.db.get(query)
            if result is None:
                self.return_internal_err("error")
            else:
                obj = self.convert_result_to_obj(result)
                for item in obj:
                    dish_ing_list = self.ing_service.get_all_dish_ingerients(item['id'])
                    if dish_ing_list:
                        item['ingredients'] = dish_ing_list
                return self.return_success(self.convert_result_to_obj(obj))
        return self.return_internal_err("error")

    def convert_result_to_obj(self, result):
        lst = []
        for res in result:
            lst.append({
                'id': res[0],
                'name': res[1],
                'calories': res[2],
                'recipe': res[3],
                'peopleCount': res[4],
                'cookingTime': res[5],
                'photoLink': res[6]
            })
        return lst

    def validate_and_convert_dish(self, dish):
        if 'name' not in dish:
            return None
        if 'recipe' not in dish:
            return None
        if 'peopleCount' not in dish:
            return None
        if 'cookingTime' not in dish:
            return None
        if 'photoLink' not in dish:
            return None
        if 'calories' not in dish:
            return None
        return (
            0, dish['name'], dish['recipe'], dish['peopleCount'], dish['cookingTime'], dish['calires'],
            dish['photoLink'])
