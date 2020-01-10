from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'First name' ,'autofocus': True, 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last name' ,'autofocus': True, 'required': True}),
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username' ,'autofocus': True, 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email', 'required': True})
        }

    # Validating password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise ValidationError("Password don't match")

        return cd['password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'Username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))