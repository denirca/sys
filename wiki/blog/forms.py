from django import forms
from .models import MyPublish, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = MyPublish
        fields = ('title', 'photo', 'phone_number', 'address', 'text', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
