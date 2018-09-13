from django.shortcuts import render
from school import view_utils


def homepage(request):
    d = {'homepage': 'active'}
    privilege = view_utils.get_user_privilege(request)
    view_utils.insert_privileges(d, privilege)

    if privilege == "admin":
        return render(request, 'home/homepage_admin.html', d)
    elif privilege == "saodo":
        return render(request, 'home/homepage_saodo.html', d)
    elif privilege == "loptruong":
        return render(request, 'home/homepage_loptruong.html', d)
    else:
        return render(request, 'home/homepage_guess.html', d)
