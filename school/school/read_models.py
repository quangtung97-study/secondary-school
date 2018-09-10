import bcrypt


def new_user(username, user_password_hash, privilege_name):
    return {
        'username': username,
        'userPasswordHash': user_password_hash,
        'privilegeName': privilege_name,
    }


def privilege_name_to_string(privilege_name):
    if privilege_name == 'admin':
        return 'Quản trị'
    elif privilege_name == 'saodo':
        return 'Sao đỏ'
    elif privilege_name == 'loptruong':
        return 'Lớp trưởng'
    else:
        return None


def check_password(user, password):
    if user is None or password is None:
        return False
    else:
        return bcrypt.checkpw(password.encode(),
                              user['userPasswordHash'].encode())
