from django.urls import path
from .views import *
from knox.views import LogoutView

app_name = 'users'

urlpatterns = [
    path(r'auth/login/', LoginUserView.as_view(), name='login_user'),
    path(r'auth/register/', RegisterUserView.as_view(), name='register_user'),
    path(r'auth/logout/', LogoutView.as_view(), name='logout'),
    path(r'auth/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path(r'auth/user/', GetAuthUserView.as_view(), name='get_user'),
]
