from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, QueryDict


def login(request):
    activate = {
        'homepage': '',
        'login': 'active',
    }
    return render(request, 'login/login.html', {'activate': activate})

@csrf_protect
def login_post(request):
    query = QueryDict(request.body)
    return render(request, 'login/login-error.html')
    # return redirect("/login")
