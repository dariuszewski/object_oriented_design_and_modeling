from itertools import product
from datetime import date, datetime


class VendingMachine:

    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def fillup(self, products):
        return product_catalog.add_products()
    
    def create_cart(self, *products):
        self.cart = [p for p in products]

    def sell_cart(self):
        if self.cart:
            return True

class Clerk:
    
    cart = []
    balance = []
    KNOWN_TOKENS = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]

    def add_to_cart(self, product):
        pass

    def add_to_balance(self, token):
        pass



class ProductCatalog:

    def __init__(self, products=None):

        self.products = []
        ProductCatalog.add_products(self, products)

    def add_products(self, products):

        for product in products:
            if isinstance(product, Product):
                if True: #self.check_date(product):
                    self.products.append(product)
                else:
                    print(f'{product} discharged, expired.')
            else:
                print(f'Invalid product: {product}')
                
   
    def clean_products(self):

        self.products = [product for product in self.products if self.check_date(product)]

    def display_products(self):

        self.clean_products()

        result = {}

        for product in self.products:
            if product.name in result:
                result[product.name]["quantity"] += 1
            else:
                result[product.name] = {"price": product.price, "quantity": 1}

        return result

    def check_date(self, product):

        if product.expiration_date > date.today():
            return True
        else:
            print(f'{product} discharged, expired.')
            return False




class Product:
    
    def __init__(self, name, price, date):

        # don't look before you leap
        try:       
            self._name = str(name)
            self._price = float(price)
            self.expiration_date = date

        except ValueError:
            raise ValueError(f"Product price must be int or float, not {type(price)}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        pass

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price
            

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.expiration_date})"

class VendingMachine:

    def __init__(self, product_catalog):
        self.product_catalog = product_catalog

    def fillup(self, products):
        return product_catalog.add_products()
    
    def create_cart(self, *products):
        self.cart = [p for p in products]

    def sell_cart(self):
        if self.cart:
            return True
            
class Cart(ProductCatalog):

    def __init__(self):
        self.products = []
        self.price = 0

    def add_to_cart(self, product):
        self.cart.append(product)
        self.price += product.price

    def remove_from_cart(self, product):
        self.cart.remove(product)
        self.price -= product.price


class Checkout:
    pass


p = Product('cola', 3, date(2022, 1, 24))
p2 = Product('fanta', 3, date(2022, 1, 16))
p3 = Product('cola', 3, date(2022, 1, 24))

cp = ProductCatalog([p, p2, p3])

v = VendingMachine(cp)

print(cp.products)
cp.clean_products()
print(cp.products)

cp.display_products()

c = Cart()
c.add_to_cart(p)
c.display_products()