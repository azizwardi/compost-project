from django.urls import path
from . import views

urlpatterns = [
    path('', views.userinterface, name='user_interface'),
]