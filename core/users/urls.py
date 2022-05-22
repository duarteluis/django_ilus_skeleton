from django.urls import path
from .views import logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='users/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
]
