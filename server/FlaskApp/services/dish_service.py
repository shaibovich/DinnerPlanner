from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels.dish import insert, get_dish_id, get
from FlaskApp.mysql.tabels import dish_ingridents
from FlaskApp.mysql.tabels import user_recipe
from FlaskApp.mysql.tabels.dish_ingridents import get_dish_with_ing
from FlaskApp.services.ingridents_service import ingridents_service as ingridents_services




class dish_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)
        self.ing_service = ingridents_services(my_sql)

    def add_dish(self, dish):
        query = insert(dish)
        id = self.db.insert(query)
        if len(list(dish['ingredients'])):
            query = dish_ingridents.insert_many(id, dish['ingredients'])
            self.db.insert(query)
        return self.return_success(dish)

    def search_dish(self, dish):
        query = get(dish)
        result = self.db.get(query)
        obj = self.convert_result_to_obj(result)
        for item in obj:
            dish_ing_list = self.ing_service.get_all_dish_ingerients(item['id'])
            if dish_ing_list:
                item['ingredients'] = dish_ing_list
        return self.return_success(obj)

    def get_user_recipes(self, user_id):
        query = user_recipe.get_all_user_recipes(user_id)
        result = self.convert_result_to_obj(self.db.get(query))
        for dish in result:
            dish_ing_list = self.ing_service.get_all_dish_ingerients(dish['id'])
            if dish_ing_list:
                dish['ingredients'] = dish_ing_list
        return self.return_success(result)

    # def delete_user_recipe(self, user_id, dish_id):
    #     query =

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

    def search_dish_without_ings(self, dish, ing_lst):
        if ing_lst is None:
            return self.search_dish(dish)
        query = get(dish)
        result1 = self.db.get(query)
        obj = self.convert_result_to_obj(result1)
        for ing in ing_lst:
            query2 = get_dish_with_ing(dish, ing)
            result2 = self.db.get(query2)
            obj2 = self.convert_result_to_obj(result2)
            for element in obj:
                if element in obj2:
                    obj.remove(element)
        for item in obj:
            dish_ing_list = self.ing_service.get_all_dish_ingerients(item['id'])
            if dish_ing_list:
                item['ingredients'] = dish_ing_list
        return self.return_success(obj)
