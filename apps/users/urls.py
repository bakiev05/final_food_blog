from django.urls import path
from apps.users.views import UserCreateView, UserLogin, user_posts
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:id>', user_posts, name='profile'),


]
