from django.urls import path
from accounts.api.views import (
                        ProfileView,
                        UpdatePassword,
                        CreateUserView
                        )

app_name = "accounts"


urlpatterns = [
    path('me', ProfileView.as_view(), name='me'),
    path('change-password', UpdatePassword.as_view(), name='change-password'),
    path('register', CreateUserView.as_view(), name='register'),
]

"""
Content is
{
"new_password": "123456",
"old_password": "123456"
}
"""