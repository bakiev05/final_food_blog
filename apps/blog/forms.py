from django import forms
from apps.blog.models import Recipe, Post


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        exclude = ['create_at', 'author']
        model = Post
        fields = '__all__'
