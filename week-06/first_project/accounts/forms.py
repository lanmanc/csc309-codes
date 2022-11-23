from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        data = super().clean()

        if len(data.get('username')) < 4:
            self.add_error('username', 'Username must be at least 4 characters')
        if data.get('password') != data.get('password2'):
            self.add_error('password2', 'Passwords do not match')
        if User.objects.filter(username=data.get('username')).exists():
            self.add_error('username', 'Username already exists')

        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self):
        data = super().clean()

        if not (user := authenticate(username=data.get('username'), password=data.get('password'))):
            self.add_error('password', 'Username or password is wrong')

        data['user'] = user

        return data
