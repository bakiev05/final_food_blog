from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from apps.users.forms import UserRegistrationForm
from apps.users.models import User
from apps.blog.models import Post


class UserCreateView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLogin(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


def user_posts(request, id):
    user_obj = get_object_or_404(User, id=id)
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'user/user_posts.html', locals())



