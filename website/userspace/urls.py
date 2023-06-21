from django.urls import path
from . import views
from django.contrib.auth import views as mdp




urlpatterns = [
    path('<str:pseudo>/projectlist', views.projectlist, name='projectlist'),
    path('<str:pseudo>/<int:idbutton>', views.userinterface, name='user_interface'),
    path('reset_password/', mdp.PasswordResetView.as_view(template_name='app/password_reset.html'), name="password-reset"),
    path('reset_password_done/', mdp.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', mdp.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', mdp.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    #path('mqttt/<int:idbutton>', views.mqttt, name='mqttt'),
    path('mq/<int:idbutton>', views.mq, name='mq'),


]