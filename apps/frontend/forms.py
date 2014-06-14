from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

class LoginForm(forms.Form):
    email = forms.EmailField(help_text='Enter Your Email ID', label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email ID', 'class': 'form-control'}))
    password = forms.CharField(help_text='Enter Your Password', label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def authenticate(self, request = None):
        logout(request)                             # logout other user
        data = self.cleaned_data
        user = authenticate(username = data['email'], password = data['password'])
        if user is not None:
            login(request, user)                    # login user
        return user