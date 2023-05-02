from django.urls import path
from . import views

urlpatterns = [
    path('<str:pseudo>', views.userinterface, name='user_interface'),
]