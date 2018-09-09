def get_user_privilege(request):
    try:
        return request.session['privilegeName']
    except KeyError as e:
        return None


def get_username(request):
    try:
        return request.session['username']
    except KeyError as e:
        return None



def set_user(request, user):
    request.session['username'] = user['username']
    request.session['privilegeName'] = user['privilegeName']


def del_user(request):
    try:
        del request.session['username']
        del request.session['privilegeName']
    except KeyError as e:
        pass
