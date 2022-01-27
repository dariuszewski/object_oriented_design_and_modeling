from Product import Product

class ProductCatalog:

    def __init__(self, products):

        self.products = {}

        ProductCatalog.add_products(self, products)
        

    def add_products(self, products):

        for product in products:
            if isinstance(product, Product):

                if product.code in self.products.keys():
                    self.products[product.code]['quantity'] += product.quantity
                else:
                    self.products[product.code] = {}
                    self.products[product.code]['name'] = product.name
                    self.products[product.code]['price'] = product.price
                    self.products[product.code]['quantity'] = product.quantity


            else:
                print(f'Invalid product: {product}')
                

   

