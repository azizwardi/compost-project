from django.urls import path
from . import views

urlpatterns=[
    path('',views.compte,name='compte'),
    path('map/', views.add_node, name='add_node'),
    path('interface/', views.interface, name='interface'),
]