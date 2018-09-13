from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import QueryDict, HttpResponse
from school import view_utils
from school import read_models
from school import write_models
from school import repository


def main_page(request):
    d = {}

    privilege = view_utils.get_user_privilege(request)
    view_utils.insert_privileges(d, privilege)
    d['loptruong_active'] = 'active'

    if privilege == "loptruong":
        return render(request, 'hoctap/manage_loptruong.html', d)
    return redirect('/')


@csrf_protect
def save_row(request):
    privilege = view_utils.get_user_privilege(request)

    if privilege != "loptruong":
        return redirect('/')
    return HttpResponse("")


@csrf_protect
def remove_row(request):
    privilege = view_utils.get_user_privilege(request)

    if privilege != "loptruong":
        return redirect('/')
    return HttpResponse("")


@csrf_protect
def add_row(request):
    privilege = view_utils.get_user_privilege(request)

    if privilege != "loptruong":
        return redirect('/')
    return HttpResponse("")
