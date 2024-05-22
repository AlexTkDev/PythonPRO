from django.contrib.auth.forms import AuthenticationForm
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
