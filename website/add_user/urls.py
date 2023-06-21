from django.urls import path
from . import views

urlpatterns=[
    path('<str:psedo>',views.add_project,name='add_project'),
    path('<str:id_projet>/<str:psedo>/add',views.compte,name='compte'),
    path('<str:id_projet>/<str:psedo>/map', views.add_node, name='add_node'),  
]