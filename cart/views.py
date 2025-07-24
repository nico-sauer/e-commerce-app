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
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))


		product = get_object_or_404(Product, id=product_id)
		cart.add(product=product, quantity=product_qty)
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Added To Cart..."))
		return response


# 2. `cart_remove` - Removes a product from the cart

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':

		product_id = int(request.POST.get('product_id'))

		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		messages.success(request, ("Removed From Cart..."))
		return response




# 3. `cart_detail` - Which displays all products already in the cart
# 4. `cart_clear` - Clears the cart completely

