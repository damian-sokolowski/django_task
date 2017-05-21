from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User


class UserForm(ModelForm):
    birthday = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birthday']
