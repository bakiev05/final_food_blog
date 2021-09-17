from django.urls import path
from apps.users.views import UserCreateView, UserLogin

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
]