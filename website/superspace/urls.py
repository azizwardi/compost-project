from django.urls import path
from . import views

urlpatterns=[
    path('<str:psedo>', views.interface, name='interface'),
]