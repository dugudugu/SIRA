from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'First name' ,'autofocus': True, 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last name' ,'autofocus': True, 'required': True}),
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username' ,  'required': True}),
        }