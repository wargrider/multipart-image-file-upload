from django import forms
from .models import Picture


class UserForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['title', 'cover', 'Description']
