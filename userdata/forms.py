from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import EmailValidator


class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=30, validators=EmailValidator)
