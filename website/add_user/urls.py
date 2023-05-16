from django.urls import path
from . import views

urlpatterns=[
    path('',views.add_project,name='add_project'),
    path('<str:id_projet>/add',views.compte,name='compte'),
    path('<str:id_projet>/map', views.add_node, name='add_node'),  
]