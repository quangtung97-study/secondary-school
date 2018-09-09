import bcrypt


def new_user(username, user_password_hash, privilege_name):
    return {
        'username': username,
        'userPasswordHash': user_password_hash,
        'privilegeName': privilege_name,
    }


def check_password(user, password):
    if user is None or password is None:
        return False
    else:
        return bcrypt.checkpw(password.encode(),
                              user['userPasswordHash'].encode())
