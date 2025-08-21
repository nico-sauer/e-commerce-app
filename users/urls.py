from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    #path("", include("django.contrib.auth.urls"))
    path("register/", views.register_user, name="register"),
    path("login_user/", views.login_user, name="login"),
    path("logout_user/", views.logout_user, name="logout"),
]


#add to urls.py in config:
#path("users"/, include('users.urls')),
#path("users/", include('django.contrib.auth.urls'))
