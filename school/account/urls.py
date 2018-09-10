from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('login/post/', views.login_post),
    path('logout/', views.logout),
    path('detail/', views.detail),
    path('change-password/', views.change_password),
    path('add-account/', views.add_account),
]
