from ProductCatalog import ProductCatalog

class VendingMachine:

    def __init__(self, product_catalog: ProductCatalog, money=10):
        self.items = product_catalog.products
        self.money = money


    def get_products(self):
        return self.items


    def vend(self, selection, item_money):
        
        if selection in self.items:            
            prod = self.items[selection]
        else:
            return f"Invalid selection! : Money in vending machine = {format(self.money, '.2f')}"

        if prod['price'] > item_money: return "Not enough money!"
        
        if prod['quantity'] < 1: return f"{prod['name']}: Out of stock!"
    
        change = prod['price'] - item_money
        self.money += prod['price']
        prod['quantity'] -= 1
        
        result = f"Vending {prod['name']}"
        
        if item_money > prod['price']:
            result = result + f" with {format(abs(change), '.2f')} change."

            
        return result
