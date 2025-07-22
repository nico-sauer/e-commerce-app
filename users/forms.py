from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    # Using the built-in form field to add validation
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["email", "password1", "password2"]