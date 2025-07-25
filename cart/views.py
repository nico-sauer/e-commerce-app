from django.shortcuts import render
from .cart import Cart
from shop.models import Product
from orders.models import Order
from users.models import CustomUser
# Create your views here.


# 1. `cart_add` - Which adds a product(or updates) to the cart

def cart_add(request):
	cart = Cart(request)

	if request.POST.get('action') == 'post':
     
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))
  
		product = get_object_or_404(Product, id=product_id)
		cart.add(product=product, quantity=product_qty)

		#messages.success(request, ("Added To Cart..."))
		return render(request, 'templates/cart/cart_add.html')


# 2. `cart_remove` - Removes a product from the cart

def cart_delete(request):
	cart = Cart(request)

	if request.POST.get('action') == 'post':

		product_id = int(request.POST.get('product_id'))
		cart.delete(product=product_id)
		#messages.success(request, ("Removed From Cart..."))
		return render(request, 'templates/cart/cart_delete.html')

# 3. `cart_detail` - Which displays all products already in the cart

def cart_detail(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		cart.__iter__
		return render(request, 'cart/cart_detail.html')


# 4. `cart_clear` - Clears the cart completely
def cart_clear(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		#product_id = int(request.POST.get('product_id'))
		cart.clear
		#messages.success(request, ("Cart Cleared..."))
		return render(request, 'templates/cart/cart_clear.html')