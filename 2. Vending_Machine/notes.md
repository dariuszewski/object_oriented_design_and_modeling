# LAB2. Vending Machine

## 1. Facade
<hr>

>`Facade` is an object that serves as a front-facing interface masking more complex underlying or structural code. When importing a module and building a code basing on that we use facade. We can think of it as assistant which can do some work for us - as pandas dataframes. They are often build to imitate real enviroment.

<br>

```
>>> import friend

>>> friend.please_buy_coffee()

coffee
```

<br>

## 2. Singleton
<hr>

>`Singleton` is a class which can have only 1 instance (it can be dictated by namesapce). If we are importing a module it is like we create a singleton - there is only one object this type and name. This is useful when exactly one object is needed to coordinate actions across the system (like Pandas library, you don't need to import it twice or like a vending machine in the system simultaing it).

<br>

## 3. Designing a solution
<hr>



 - Making 1 class for everything  is not a good design!
 - Metaphores are programmers best friends.
 - When designing a system think in object categories.
 - First we have possibilities, then we think what we can do.

 reality + technology --> methaphores --> design --> simulation --> solution
 
 <br>
 
 ### 1.  reality + technology
 <hr>

 - define a problem -> simulate vending machine
 - choose right technology for it -> Python

 <br>

 ### 2. methaphores
 <hr>

 ```
class VendingMachine:

    def __init__(self, items):
        self.items = items

class Shop:
    pass

class Product:
    pass

class ProductCatalog:
    def __init__(self, products):
        self.products = [Product(p) for p in products]

class Checkout:
    pass
 ```


### 3. design
<hr>

><b>Product</b> class should be defined above <b>ProductCatalog</b> becouse name <i>Product</i> has to be defined before use! Biggest class should be defined higher, alternatively we can (and it's a good practice) create separate modeules per class. <u>Problem</u> would be if both of theese classes would like to operate on each other (Product is a part of Catalog, and Catalog is a part of Product) - we would get into circular import error.
<br>
#### Mereology -> science of fulls and parts

Intresting thing:
```
>>> c = Checkout() 
>>> c.x = 42
>>> c.x
42
>>> o = object()
>>> o.x = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'object' object has no attribute 'x'
```


## 4. Dependency,  Aggregation & Composition
<hr>


>`dependency` is weakest type of realtionship, where one part is using other part.

>`aggregation` is a 'has-a' assosciation of objects.  It represents a part-whole and part-of relationship where parts can live together and separately

>`composition` is a stronger type of aggregation where lifetime of part-whole and part-of have common duration


But this can be considered as association:

```
>>> foo = lambda: None
>>> bar = lambda: None 
>>> foo.bar = bar
>>> del bar
>>> foo.bar
<function <lambda> at 0x000002A22B21E5F0>
```

