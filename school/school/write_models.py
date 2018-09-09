from . import read_models
import bcrypt


def new_user(username, password, privilege_name):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    if privilege_name == "saodo":
        privilege_id = 2
    elif privilege_name == "loptruong":
        privilege_id = 3
    else:
        return None

    return {
        'username': username,
        'userPasswordHash': hashed.decode(),
        "privilegeId": privilege_id,
    }


check_password = read_models.check_password


def new_removing_user(username):
    return {'username': username, }
