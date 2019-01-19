from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels import user_recipe

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

