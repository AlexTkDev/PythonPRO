from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from messenger_app.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "например, Megamozg"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "*******************"
    }))

    class Meta:
        model = User
        fields = ('username', 'password')



class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "например, Megamozg"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "например, Megamozg@gmail.com"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "*******************"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control", "placeholder": "*******************"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
