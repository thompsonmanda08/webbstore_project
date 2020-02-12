from django import forms
from django.contrib.auth.models import User
from .models import UserAccount


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('profile_photo', 'address')
