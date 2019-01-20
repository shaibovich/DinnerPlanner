from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels.users import get, insert


class user_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)

    def login(self, user):
        self.validate_login_and_convert(user)
        query , params= get(user)
        result = self.db.get(query, params)
        if result and len(result):
            response = {
                'id': result[0][0],
                'email': result[0][1],
                'name': result[0][2],
                'password': result[0][3]
            }
            return self.return_success(response)
        else:
            return self.return_internal_err("Invalid Email / Password")

    def signup(self, user):
        self.validate_signup(user)
        query, params = insert(user)
        id = self.db.insert(query, params)
        response = {
            'id': id,
            'email': user['email'],
            'name': user['user'],
            'password': user['password']
        }
        return self.return_success(response)

    def validate_login_and_convert(self, user):
        if 'email' not in user:
            self.return_validation_err("validation error for login")
        if 'password' not in user:
            self.return_validation_err("validation error for login")

    def validate_signup(self, user):
        if 'email' not in user:
            self.return_validation_err("validation error for signup")
        if 'password' not in user:
            self.return_validation_err("validation error for signup")
        if 'user' not in user:
            self.return_validation_err("validation error for signup")
