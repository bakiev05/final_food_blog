from django import forms
from apps.replies.models import Reply


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ['post', 'user']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'text'}),

        }
