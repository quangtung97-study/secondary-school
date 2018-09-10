from . import read_models
import bcrypt


def new_user(username, password, privilege_name):
    if username is None or password is None or privilege_name is None:
        return None

    if len(username) > 50:
        return None

    if len(password) < 4:
        return None

    if privilege_name not in ['admin', 'saodo', 'loptruong']:
        return None

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return {
        'username': username,
        'userPasswordHash': hashed.decode(),
        "privilegeName": privilege_name,
    }


# check_password(user, password)
check_password = read_models.check_password


def new_removing_user(username):
    return {'username': username, }


# Return None if not success
def get_new_user_after_change_password(
    old_user,
    old_password,
    new_password,
    re_enter_new_password
):
    if old_user is None:
        return None
    if old_password is None or new_password is None:
        return None
    if new_password != re_enter_new_password:
        return None

    ret = check_password(old_user, old_password)
    if ret is False:
        return None

    return new_user(
        username=old_user['username'],
        password=new_password,
        privilege_name=old_user['privilegeName']
    )


def new_user_for_adding(username, password,
                        re_enter_password, privilege_name):
    if password != re_enter_password:
        return None
    user = new_user(username, password, privilege_name)
    if user is None:
        return None
    if user['privilegeName'] == 'admin':
        return None
    return user
