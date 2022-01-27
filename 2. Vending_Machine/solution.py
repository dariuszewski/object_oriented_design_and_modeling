class VendingMachine():

    def __init__(self, items, money, credit=0):
        self.items = items
        self.money = money

    def vend(self, selection, item_money):
        
        if selection in [item['code'] for item in self.items]:            
            prod = list(filter(lambda el: el['code'] == selection, self.items))[0]
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

        