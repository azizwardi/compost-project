from django.urls import path
from . import views

urlpatterns=[
    path('',views.compte,name='compte'),
    path('<str:pseudo>/map', views.add_node, name='add_node'),
]