from django.urls import path, include
from .views import *



urlpatterns = [
    path('register/', RegisterApi.as_view(), name= "register"),
    path("login/", UserLoginApi.as_view(), name= "login"), 

    path("profile/", ProfileAPi.as_view()),
    path("change-password/", ChangePassword.as_view()),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),




]
