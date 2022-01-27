#złamanie zasady pojedynczej odpowiedzialnosci spowodowalo
#ze w wynikach mamy jakies chore liczby

import os
PRICE = 11
class StockBar:

    def __init__(self, unit_weight):
        self.unit_weight = unit_weight

    def calculate_weight(self, length):
        weight = length * self.unit_weight
        return weight


    def calculate_price(self, length, unit_price=None):
        if unit_price is None:
            unit_price = os.getenv('PRICE', 1) #PRICE #
        unit_price = self.refine_unit_price(unit_price)
        price = self.calculate_weight(length) * unit_price
        return price
    
    def refine_unit_price(self, price):
        return price
    
    

class SaleStockBar(StockBar):

    def __init__(self, weight_adj, price_adj, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weight_adj = weight_adj
        self.price_adj = price_adj
    

    def calculate_weight(self, length):
        length = float(length)
        if length < 0:
            raise ValueError('Length must be positive')
        weight = length * self.unit_weight
        return weight

    def calculate_weight(self, *args, **kwargs):
        return super().calculate_weight(*args, **kwargs) * self.weight_adj

    def calculate_price(self, length, unit_price=None, *args, **kwargs):
        if unit_price is None and 'PRICE' not in os.environ:
            raise RuntimeError('No price in env vars')
        original_price =  super().refine_calculate_price(length, unit_price=None, *args, **kwargs) * self.price_adj
        price = original_price * self.price_adj
        return round(price)
        #return dict(original=original_price, refined=price)

    def refine_unit_price(self, price):
        price = super().refine_unit_price(price)
        return max(price, 20)

    def set_unit_weight(self, new_weight):
        self.unit_weight = new_weight

class Clerk:

    @staticmethod
    def format_message(code, value):
        messages = {
            'Weight' : 'Masa odcinka wynosi {} kg',
            'Price' : 'Cena odcinka wynosi {:.2f} zł',
        }
        print(messages[code].format(value))



foo=SaleStockBar(3)
bar=SaleStockBar(1, 1.2, 3)

Clerk.format_message('Price', foo.calculate_price(2))
Clerk.format_message('Price', bar.calculate_price(2))