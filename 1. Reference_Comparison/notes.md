# LAB1. Height Problem Solver

## 1. Classes Naming Conventions
<hr>

- If class refers to something very abstract, it is good practice to named it after something it <i>has</i> or <i> does</i>

- Example: class which represents something that have height, so it can be either person, building and many more

```
class HeightObservable:

    def __init__(self, height):
        self.height = height
```

## 2. Interfaces
<hr>

### What is interface?
- a collection of method / attribute signatures that have to be provided by the implementing class, for example class like <b>Person</b> or <b>Building</b> inheriting from <b>HeightObservable</b> should have provied <i>height</i> attribute.

- we should not (and in different languages can't) create objects based on interface itself.

- implementation will be done by children inheriting from interface like below

```
class Human(HeightObservable):
    pass

foo = Human()
```
```
TypeError: HeightObservable.__init__() missing 1 required positional argument: 'height'
```
- to see all methods of a class or object call:

```
Human.__dir__()
```

## 3. Method Resolution Order
<hr>


```
Human.__mro__
```
```
(<class '__main__.Human'>, <class '__main__.HeightObservable'>, <class 'object'>)
```
- `__mro__` returns a tuple which indicies represents inheritance order of attribute search

- it can be modified on class level only

## 4. `isinstance()` & `hasattr()`
<hr>

```
foo = Human(180)
bar = lambda: None
moo = Human.__init__(bar, 190)
```
>foo and moo are both passed <b>Human</b> class initialization and they both have access to <i>height</i> attribute, but moo is actually NOT a <b>Human</b> instance. If we would like verify if they have access to it by:

```
if isinstance(foo, Human):
    return foo.height
```
>the test will FAIL for moo, but it actually have access to it, so it is a common practice to instead use:

```
if hasattr(foo, 'height'):
    return foo.height
```
>in general 'Look-Before-You-Leap' is not Pythonic approach, usually programmers type:
```
try:
    foo.height
except AttributeError:
    raise ...
```

## 5. Operator Overloading
<hr>

- there is usually no point of implementing all operators, instead it is enough to use :
    - `@TotalOrdering` decorator
    - `__lt__` operator
    - `__eq__` operator

<br>
<u>Decorators</u>

>- they are applied to whatever is defined below them eg. classes or functions
>- they are injesting higher order functions to them 
>- they returns same but modified object and makes sure that the result will be bind to the same name
>- in case of `@total_ordering` it is ingestion of other comparison operator basing on 2 provided.

<br>

```
from functools import total_ordering

@total_ordering
class NamedHeight:
    
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height < other.height   
```

>There is a difference in mathematical value and identity

```
Bob = NamedHeight('Bob', 170)
Alice = NamedHeight('Alice', 170)

Bob == Alice
>>> True

Bob is Alice
>>> False
```

> Extreme situation would be if height was equal to: `float('nan')`. Then `Bob == Bob` would return false.

> `is` is 'kind-of-a' reference operator and also can be overloaded. 

## 6. Hashable Types
<hr>


```
>>> {Alice, Bob}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'NamedHeight'
```
We cannot create a set of objects becouse they are not treated as unique AT THIS POINT -> they don't have their hash, but if we wouldn't have `@total_ordering` and `__eq__` they would could.

<br>

> <u>Hashable types are:</u>
> - representing elements where each object is seen as an identity, not space in memory like objects do.
> - to make objects hashable use `__hash__(self)`
> - it is recommended for hash to be a number
> - hash is a part of identity which can be observed and compared in True / False manner

<br>

```
from functools import total_ordering

@total_ordering
class NamedHeight:
    
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height < other.height   

    def __hash__(self, other):
        return self.height
```

```
>>> Bob = Child('Bob', 20)
>>> Alice = Child('Alice', 20)
>>> mySet = {Alice,Bob}
>>> mySet
{<__main__.NamedHeight object at 0x000001D0B3C074F0>}
>>> next(iter(mySet)).name
'Alice'
```

## 7. Building Solution
<hr>

the problem is based on table of truth which can be represented as following:

```
def correct(self):
    try:
        return all((
            self.W > self.D,
            self.W < self.Z,
            self.L > self.B,
            self.L < self.D,
            self.L < self.W,
            self.B != min(self._all)
        ))
    except AttributeError:
        return False
```
names represented by their first letters were given in the problem description.

<br>

children are stored in list. We iterate over names and setting attrubutes of current class (`Solution`) 

```
class Solution:

    def __init__(self, *args):
        self._all = args
        for arg in args:
            setattr(self, arg.name, arg)
```


now, we need a way to pass arguments as `NamedHeight objects`, we do that using `SolutionFactory` class as follows

```
class SolutionFactory:

    def __init__(self, names):
        self.names = names

    def create(self, heights):
        args = [NamedHeight(n, h) for n, h in
                zip(self.names, heights)]
        return Solution(*args)

    def __iter__(self):
        return (self.create(hs) for hs in
                permutations(range(len(self.names))))

factory = SolutionFactory(
    ['W', 'D', 'Z', 'L', 'B', 'K'])
```

We create a text representation of `solution` obcject in `Solution` class


```
    def __str__(self):
        return ' | '.join(
            f'{c.name} {c.height}' for c 
            in sorted(self._all, reverse=True))
```


at the and we are looking for correct solution in the factory.
```
for solution in factory:
    if solution.correct():
        print(solution)

Z 5 | W 4 | D 3 | L 2 | B 1 | K 0
```

