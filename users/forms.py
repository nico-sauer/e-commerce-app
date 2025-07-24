from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    # Using the built-in form field to add validation
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = 
        ["first_name", "last_name",
         "username",
         "email",
         "password1",
        "password2"]
        
  
#check if we have to add loginform or there is built in function
        
# class LoginForm(AuthenticationForm):
#     username = UsernameField(label='Enter Username',
#                              widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(label='Enter Password',
#                                widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    
# or we can use built in form AuthenticationForm()
