from django.urls import path
from . import views

urlpatterns = [
    path('', views.login2, name='user_login'),
]