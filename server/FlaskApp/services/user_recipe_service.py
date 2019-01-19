from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels import user_recipe, meal_dishes

class user_recipe_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)


    def add_or_update_dish(self, request):
        query = user_recipe.get_user_recipe(request['user'], request['dish_id'])
        if self.db.is_exists(query):
            query = user_recipe.update_recipe(request)
        else:
            query = user_recipe.insert(request)
        result = self.db.insert(query)
        return self.return_success(result)


    def delete_dish_recipe(self, user_id, dish_id):
        query = user_recipe.delete_user_recipe(user_id,dish_id)
        self.db.delete(query)
        return self.return_success('success')


