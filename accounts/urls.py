from django.urls import path

from .views import (
    LoginView, LogoutView, ProfileView, RegisterView, PasswordResetView)

base_dir = 'guruable/accounts/'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name=base_dir + 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('profile/', ProfileView.as_view(
    #     template_name=base_dir + 'profile.html'), name='profile'),
    path('register/', RegisterView.as_view(
        template_name=base_dir + 'register.html'), name='register'),
    path('reset-password/', PasswordResetView.as_view(
        template_name=base_dir + 'reset-password.html'),
        name='reset-password')
]
