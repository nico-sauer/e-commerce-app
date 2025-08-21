#from django.db import models
#from django.conf import settings
from shop.models import Product
# from orders.models import Order
# from users.models import CustomUser

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
        # product_id = str(product.id)
        # product_qty = self.quantity

        # if product_id in self.cart: #overide_quantity 
        #     new_qty = quantity + product_qty
        #     self.cart[product_id]['quantity'] = new_qty
        #     override_quantity = True
        #     return override_quantity
        

        # else:
        #     self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
            
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        

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

        self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = float(item['price'])
            item['total_price'] = float(item['price']) * item['quantity']
        yield item


    def __len__(self):
        """
        Count all items in the cart.
        """
        return len(self.cart)

    def get_total_price(self):
        
        #get product ids, look up in database and calculate total_price price
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart()
        
        for k, v in quantities.items():
            k = int(k)
            for product in products:
                if product.id == k:
                    total_price = product.price * v
        return total_price


    def clear(self):
        """Removes cart from the session."""
    
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            if product.quantity > 0:
                del self.cart[product] 
                        
        #del self.cart['session_key'] (#or just deleting the full session like this ??idk)
        self.save()    
        

    def get_discount(self):
        #coupon code field/form? 
        pass

    def get_total_price_after_discount(self, total_price, discount):
        
        # price_after_discount = total_price * discount / 100
        # return price_after_discount
        pass
    