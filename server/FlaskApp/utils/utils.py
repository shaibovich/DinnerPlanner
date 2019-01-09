# This file will be the util file for the server


def validate_user(user):
    #here we need to validate the user data
    print(user)
    return 1


def validate_request(request):
    if not request.is_json:
        return False
    if request.json is None:
        return False
    return True

def validate_signup(user):
    if 'email' not in user:
        return False
    if 'password' not in user:
        return False
    if 'user' not in user:
        return False
    del user['rememberMe']
    return True



def validate_login(user):
    if 'email' not in user:
        return False
    if 'password' not in user:
        return False
    return True
