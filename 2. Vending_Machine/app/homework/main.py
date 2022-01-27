from Product import Product
from VendingMachine import VendingMachine, ProductCatalog




products = [
Product('DC1', 'Dark Choclate', 3.59, 1),
Product('MC1', 'Milk Choclate', 3.59, 10),
Product('PB1','Penaut Bar', 3, 10)
]

vm = VendingMachine(ProductCatalog(products))
vm.get_products()

vm.vend('DC1', 3.59)
vm.get_products()

