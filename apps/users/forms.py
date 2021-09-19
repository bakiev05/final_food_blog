from django import forms
from apps.users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = (
        #     'username',
        #     'email',
        #     'age',
        #     'bio',
        #     'gender',
        #     'profile'
        # )

    widgets = {
        'username': forms.TextInput(attrs={'class': "form-control"}),
        'profile': forms.FileInput(attrs={'class': "form-control"}),
        'bio': forms.TextInput(attrs={'class': 'form-control'}),
        'age': forms.NumberInput(attrs={'class': 'form-control'}),
        'gender': forms.Select(attrs={'class': 'form-control'}),
    }