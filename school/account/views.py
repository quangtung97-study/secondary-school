from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import QueryDict
from school import read_models
from school import write_models
from school import repository
from school import view_utils


def login(request):
    if view_utils.get_user_privilege(request) is None:
        return render(request, 'account/login.html')
    else:
        return redirect('/')


@csrf_protect
def login_post(request):
    query = QueryDict(request.body)
    username = query['username']
    if username is None:
        return render(request, 'account/login-error.html')

    user = repository.get_user_by_name(username)

    if read_models.check_password(user, query['password']):
        view_utils.set_user(request, user)
        return redirect("/")

    return render(request, 'account/login-error.html')


@csrf_protect
def logout(request):
    view_utils.del_user(request)
    return redirect('/')


def detail(request):
    d = {
        'username': view_utils.get_username(request),
        'privilege': view_utils.get_user_privilege_string(request),
    }
    privilege = view_utils.get_user_privilege(request)
    view_utils.insert_privileges(d, privilege)

    if privilege is None:
        return redirect('/')
    elif privilege == "admin":
        users = repository.get_users_except_admin()
        d['users'] = users
        return render(request, 'account/detail_admin.html', d)
    else:
        return render(request, 'account/detail_normal.html', d)


@csrf_protect
def change_password(request):
    privilege = view_utils.get_user_privilege(request)
    if privilege == None:
        return redirect('/')

    query = QueryDict(request.body)

    ret = repository.update_password(
        username=view_utils.get_username(request),
        old_password=query['old-password'],
        new_password=query['new-password'],
        re_enter_new_password=query['re-enter-new-password']
    )
    if ret is False:
        return render(request, 'account/change-password-error.html')

    return redirect('/account/detail/#change-password')


@csrf_protect
def add_user(request):
    privilege = view_utils.get_user_privilege(request)
    if privilege != 'admin':
        return redirect('/')

    query = QueryDict(request.body)

    ret = repository.add_user(
        username=query['username'],
        password=query['password'],
        re_enter_password=query['re-enter-password'],
        privilege_name=query['privilege-name']
    )

    if ret is False:
        return render(request, 'account/add-account-error.html')

    return redirect('/account/detail/#add-user')


#csrf_protect
def remove_users(request):
    privilege = view_utils.get_user_privilege(request)
    if privilege != 'admin':
        return redirect('/')

    query = QueryDict(request.body)
    usernames = query.getlist('user-list')
    usernames = write_models.validate_usernames(usernames)
    repository.remove_users(usernames)
    return redirect('/account/detail/#remove-users')
