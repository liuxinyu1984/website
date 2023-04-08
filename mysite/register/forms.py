from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(help_text="Email is <strong>required</strong> to reset your password.")
    #wechat_id = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
