class Product:
    
    def __init__(self, code, name, price, quantity=1):

        # don't look before you leap
        try:    
            self._code = str(code)   
            self._name = str(name)
            self._price = float(price)
            self._quantity = int(quantity)

        except ValueError:
            raise ValueError(f"Product price must be int or float, not {type(price)}")


    @property
    def code(self):
        return self._code    

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def __repr__(self):
        return f"Product('{self.code}', '{self.name}', {self.price})"


