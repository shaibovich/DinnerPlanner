from services.abstract_service import abstrac_service
from mysql.tabels.dish import insert, get_dish_id, get, full_get_dish
from mysql.tabels import dish_ingridents
from mysql.tabels import user_recipe

from services.ingridents_service import ingridents_service as ingridents_services


class dish_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)
        self.ing_service = ingridents_services(my_sql)

    def add_dish(self, dish):
        query, params = insert(dish)
        id = self.db.insert(query, params)
        if len(list(dish['ingredients'])):
            query, params = dish_ingridents.insert_many(id, dish['ingredients'])
            self.db.insert(query, params)
        return self.return_success(dish)

    def search_dish(self, dish):
        query = full_get_dish(dish, dish['filter']['calories'], dish['filter']['cookingTime'],
                              dish['filter']['withIngredient'], dish['filter']['withoutIngredient'])
        result = self.db.get(query, ())
        obj = self.convert_result_to_obj(result)
        for item in obj:
            dish_ing_list = self.ing_service.get_all_dish_ingerients(item['id'])
            if dish_ing_list:
                item['ingredients'] = dish_ing_list
        return self.return_success(obj)

    def get_user_recipes(self, user_id):
        query, params = user_recipe.get_all_user_recipes(user_id)
        result = self.convert_result_to_obj(self.db.get(query, params))
        for dish in result:
            dish_ing_list = self.ing_service.get_all_dish_ingerients(dish['id'])
            if dish_ing_list:
                dish['ingredients'] = dish_ing_list
        return self.return_success(result)

    def to_recipes_list(self, recipes):
        lst = []
        for recipe in recipes:
            lst.append({
                'id': recipe[0],
                'name': recipe[1],
                'calories': recipe[2]
            })

        return lst

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

    def import_dishes(self, dishes):
        print("Starting importing dishes")
        for dish in dishes:
            print("Import dish : {}".format(dish['name']))
            for ing in dishes['ingredients']:
                result = self.ing_service.search_ing(ing['name'])
                if result is None:
                    print("No ingredient with name : {} - adding".format(ing['name']))
                    id = self.ing_service.add_ingrident(ing)
                    ing['id'] = id
                else:
                    ing['id'] = result['id']

            self.add_dish(dish)
            print("Finish import dish : {}".format(dish['name']))

        return self.return_success("success")
