def get_user_privilege(request):
    return request.session.get('privilegeName', default=None)


def get_username(request):
    return request.session.get('username', default=None)


def set_user(request, user):
    request.session['username'] = user['username']
    request.session['privilegeName'] = user['privilegeName']
    request.session.modified = True


def del_user(request):
    request.session.flush()
