from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels.users import get, insert



class user_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)

    def login(self, user):
        obj = self.validate_login_and_convert(user)
        if obj is None:
            return self.return_validation_err("User is invalid : {}".format(user))
        query = get(user)
        result = self.db.get(query)
        if result and len(result):
            response = {
                'id': result[0][0],
                'email': result[0][1],
                'name': result[0][2],
                'password': result[0][3]
            }
            return self.return_success(response)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def signup(self, user):
        obj = self.validate_signup(user)
        if obj is None:
            return self.return_validation_err("User is invalid : {}".format(user))
        query = insert(user)
        if self.db.insert(query):
            return self.return_success(user)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def validate_login_and_convert(self, user):
        if 'email' not in user:
            return None
        if 'password' not in user:
            return None
        return (
            user['email'],
            user['password']
        )

    def validate_signup(self, user):
        if 'email' not in user:
            return None
        if 'password' not in user:
            return None
        if 'user' not in user:
            return None
        return (
            user['email'],
            user['user'],
            user['password']
        )
