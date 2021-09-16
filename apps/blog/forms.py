from django import forms
from django.forms.models import inlineformset_factory
from apps.blog.models import Recipe, RecipeVideo, \
    Post, \
    PostImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeVideoForm(forms.ModelForm):
    class Meta:
        model = RecipeVideo
        fields = ['video']


class PostForm(forms.ModelForm):
    class Meta:
        exclude = ['create_at']
        model = Post
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


PostImageFormSet = inlineformset_factory(Post,
                                         PostImage,
                                         form=PostImageForm,
                                         extra=2,
                                         )
