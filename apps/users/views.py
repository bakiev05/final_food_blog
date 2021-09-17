from apps.users.forms import UserRegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class UserCreateView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLogin(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
