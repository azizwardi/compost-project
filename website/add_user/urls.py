from django.urls import path
from . import views

urlpatterns=[
    path('',views.add_project,name='add_project'),
    path('add',views.compte,name='compte'),
    path('<str:pseudo>/map', views.add_node, name='add_node'),
]