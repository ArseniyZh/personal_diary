from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Post


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {
            'title': 'Введите заголовок записи',
            'text': 'Введите содержание заметки'
        }


class EditPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_changed']
        labels = {
            'title': 'Введите заголовок записи',
            'text': 'Введите содержание заметки'
        }