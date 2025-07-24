from django.db import models
from shop.models import Product
from orders.models import Order
from users.models import CustomUser

class Cart(object):  # Request object
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
		self.request = request
		cart = self.session.get('session_key')

		# if no session -> start session  
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}
		self.cart = cart

    
    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
		product_qty = str(quantity)
		
		if product_id in self.cart: #overide_quantity 
			self.cart[product_id] = int(product_qty)
        
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)

		save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product)
		if product_id in self.cart:
			del self.cart[product_id]

		save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		return products


    def __len__(self):
        """
        Count all items in the cart.
        """
        return len(self.cart)

    def get_total_price(self):
        
        #get product ids, look up in database and calculate total_price price
		product_ids = self.cart.keys()
		products = Product.objects.filter(id__in=product_ids)
		quantities = self.cart
		total_price = 0
		
		for k, v in quantities.items():
			k = int(k)
			for product in products:
				if product.id == k:
					if product.is_sale:
						total_price = total_price + (product.sale_price * v)
					else:
						total_price = total_price + (product.price * v)

		return total_price


    def clear(self, product):
        """Removes cart from the session."""
    
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
           for product, in products:
               if product.quantity > 0:
                   del self.cart[product] 
                   #??? yea idk bro
                   
        #del self.cart['session_key'] #or just deleting the full session ??
                   
               
		save()
  
  

    def get_discount(self):
        pass

    def get_total_price_after_discount(self):
        pass
