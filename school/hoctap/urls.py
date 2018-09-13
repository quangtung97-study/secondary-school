from django.urls import path
from . import views

urlpatterns = [
    path('save-row/', views.save_row),
    # path('remove-row/', views.remove_row),
    # path('add-row/', views.add_row),
    path('', views.main_page),
]
