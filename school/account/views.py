from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import QueryDict
from school import read_models
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
    d = {'username': view_utils.get_username(request)}
    privilege = view_utils.get_user_privilege(request)
    if privilege is None:
        return redirect('/')
    elif privilege == "admin":
        return render(request, 'account/detail_admin.html', d)
    else:
        return render(request, 'account/detail_normal.html', d)


@csrf_protect
def change_password(request):
    query = QueryDict(request.body)

    ret = repository.update_password(
        username=view_utils.get_username(request),
        old_password=query['old-password'],
        new_password=query['new-password'],
        re_enter_new_password=query['re-enter-new-password']
    )
    if ret is False:
        return render(request, 'account/change-password-error.html')

    return redirect('/account/detail/')
