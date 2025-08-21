from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
   
    path("products/", views.product_list, name="products"),
]