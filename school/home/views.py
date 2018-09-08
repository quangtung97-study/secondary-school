from django.shortcuts import render


def homepage(request):
    activate = {
        'homepage': 'active',
    }
    return render(request, 'home/homepage.html', {'activate': activate})
