from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    # placeholder for debugging needs to be order form
    name = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["first_name",
        "last_name", 
        "email", 
        "password1",
        "password2"]
        