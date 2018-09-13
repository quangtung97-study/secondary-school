from school import read_models


def get_user_privilege(request):
    return request.session.get('privilegeName', default=None)


def get_user_privilege_string(request):
    privilege_name = request.session.get('privilegeName', default=None)
    return read_models.privilege_name_to_string(privilege_name)


def get_username(request):
    return request.session.get('username', default=None)


def set_user(request, user):
    request.session['username'] = user['username']
    request.session['privilegeName'] = user['privilegeName']
    request.session.modified = True


def del_user(request):
    request.session.flush()


def insert_privileges(d, privilege):
    if privilege == 'admin':
        d['saodo_privilege'] = True
        d['loptruong_privilege'] = True
    elif privilege == 'saodo':
        d['saodo_privilege'] = True
    elif privilege == 'loptruong':
        d['loptruong_privilege'] = True
