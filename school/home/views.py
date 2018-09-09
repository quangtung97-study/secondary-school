from django.shortcuts import render
from school import view_utils


def homepage(request):
    d = {'homepage': 'active'}
    if view_utils.get_user_privilege(request) == "admin":
        return render(request, 'home/homepage_admin.html', d)
    else:
        return render(request, 'home/homepage_guess.html', d)
