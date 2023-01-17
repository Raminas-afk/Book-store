from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from .models import UserProfile


class NewUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("country", "city", "address", "phone")
