from django.urls import path
from . import views

urlpatterns = [
    path('', views.login1, name='supervisor_login'),
]