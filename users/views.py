from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm



def register_user(request):
    # Check if the form has been submitted
    if request.method == "POST":
        # inputting submitted info to the form
        form = RegisterForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username = email, password = password)
            login(request, user)
            messages.success(request, "Registration successful!")
            # Redirect to home page
            return redirect("/")
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    

def login_user(request):
    if request.method == "POST":
        
        email = request.POST['email address']
        password = request.POST['password']
        
        # email = form.cleaned_data['email address']
        # password = form.cleaned_data['password']
        user = authenticate(email = email, password = password)    
        if user is not None: 
            login(request, user)
            return redirect("/") #if not working try ("core:home")
        else:
            messages.success(request, "There was an error. Try to log in again")
            return redirect('login')
    else: 
        return render(request,'registration/login.html') #add registration/ if not working  
    
        
def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect('index')
    

    # def logged_in(request):
        