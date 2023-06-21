from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('<str:psedo>/', views.interface, name='interface'),
    path('<str:psedo>/clientslist', views.list, name='list'),
    path('<str:psedo>/delete/<int:id>/', views.delete_client, name='delete_client'),
    path('<str:psedo>/modify_2/<int:id>/', views.modify_2, name='modify_2'),
]