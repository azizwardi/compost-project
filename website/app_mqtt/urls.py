from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish_message, name='publish'),
    path('update', views.start_mqtt, name='update'),
]