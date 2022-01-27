# LAB3. It's a Zoo Distater!

## 1. Realtions
<hr>

>`retaltion`, from mathematichal perspective is a subset of cartesian product of all given elements.

<br>


for example: 

<br>


```
from itertools import product
from operator import __lt__ as lt

items = {'a' , 'b', 'c', 'd'}
pairs = product(items, items)

pairs = [*pairs]
relation = filter(lambda p: lt(*p), pairs)

[*relation]
```

This is a specific relation, returning subset of elements 
under some condidtion -> here left element of pair is less 
than right element.


This relation is:
  - anti-symmetric
  - not-back relation
  - ordered

<br>

## 2. Directed Acyclic Graphs
<hr>

>`networkx.org` -> package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

>DAGs :In mathematics, particularly graph theory, and computer science, a `directed acyclic graph` is a directed graph with no directed cycles. That is, it consists of vertices and edges, with each edge directed from one vertex to another, such that following those directions will never form a closed loop.


><i>TIP :</i> 
While writing a code, try to think in categories of `relations` and `dependencies` instead of facts and categorization. It is difficult to rely only on last two becouse real life is full of exceptions

<br>


## 3. Solving a problem (zoo disaster)
<hr>

### 1. Load 'configuration file'

The rules of <i>who-eats-who</i> are nothing else than 
specific configuration of given problem. It can always be 
changed and the program should <u>not</u> have to break 
becouse of it. We created a <i>foodchain.txt</i> file for it 
and <i>chain.py</i> to load it with following class:


```
from collections import defaultdict
from entity import Entity

class FoodChain:
    def __init__(self, pairs):
        self.relation = defaultdict(set)
        for k, v in pairs:
            self.relation[k].add(v)
```

<br>

### 2. Creating 2nd 'constructor'

In order to load foodchain from file we create second 
constructor with `@classmethod` decorator, as it will only 
work on class and won't be called on instances, naming it `from_...` is quite typical practice.

```
    @classmethod
    def from_file(cls, filepath, as_default=False):
        with open(filepath, 'rt') as file:
            lines = file.readlines()
        pairs = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            left, right = line.split(' eats ')
            pairs.append((left.strip(), right.strip()))
        return cls(pairs)

fc = FoodChain.from_file('app/foodchain.txt')
```
```
>>> fc.relation
defaultdict(<class 'set'>, {'antelope': {'grass'}, 'big-fish': {'little-fish'}, 'bug': {'leaves'}, 'bear': {'cow', 'chicken', 'sheep', 'big-fish', 'bug', 'leaves'}, 'chicken': {'bug'}, 'cow': {'grass'}, 'fox': {'chicken', 'sheep'}, 'giraffe': {'leaves'}, 'lion': {'antelope', 'cow'}, 'panda': {'leaves'}, 'sheep': {'grass'}})

```

### 3. Implementing `__contains__` ( `in` operator)

Now, we need to create a type `Entity`, we can assume we it
will have an animal name and foodchain passed to it's 
constructor.
It is a good moment to think about how we want to use this class. 

Examples:

```
fox.eats(sheep, fc)
```
```
fc.eats(fox, sheep)
```
```
sheep in fc(fox)
```

Trying to implement 3rd option we can follow this code:

#### 1.Create Entity class:
```
class Entity:

    def __init__(self, species, foodchain=None):
        self.species = species
```

#### 2. Add following function to Foodchain class:
```
    def __call__(self, entity):
        class SpeciesSet(set):
            def __contains__(self, item):
                if hasattr(item, 'species'):
                    return super().__contains__(item.species)
                return super().__contains__(item)

        if entity.species in self.relation:
            return SpeciesSet(self.relation[entity.species])
        return set()
```

#### 3. Test code
```
>>> fox = Entity('fox')
>>> sheep = Entity('sheep')
>>> sheep in fc(fox)
True
>>> fox in fc(sheep)
False
>>>
```

### 3. Implicit foodchain
Goal:
```
fox.eats(sheep)
```
#### 1. Extend Entity class

```
class Entity:

    def __init__(self, species, foodchain=None):
        self.species = species
        self.foodchain = foodchain

    def eats(self, other):
        return other in self.foodchain(self)
```

#### 2. Test code
```
>>> fox = Entity('fox', fc)
>>> sheep = Entity('sheep', fc)
>>> fox.eats(sheep)
True
```

We got to the point where configuration is passed once - in 
the initialization.<br> We can also write: 
```
>>> eaters = [fox, sheep]
>>> foods = [sheep, grass]
>>> matches = map(Entity.eats, eaters, foods)
>>> print(*matches)
True True
>>>
```

If we don't want to pass foodchain into the `Entity` we can modify a class as follows:

```
class Entity:

    DEFAULT_FOODCHAIN = None

    def __init__(self, species, foodchain=None):
        self.species = species
        self.foodchain = foodchain

    def eats(self, other):
        foodchain = self.foodchain or self.DEFAULT_FOODCHAIN
        return other in foodchain(self)
```

And then use it like:

```
fc = FoodChain.from_file('app/foodchain.txt')

Entity.DEFAULT_FOODCHAIN = fc

fox = Entity('fox')
sheep = Entity('sheep')
fox.eats(sheep)
```

## 4. Implicit better than Explicit?!
<hr>

>Every higher-level language provides some level of implicity, in right proportions and used in right situation implicity just makes code actually clearer and easier to use. Bear needs to be in in foodchain, but user actually don't know it at the first place.

> `Entity.DEFAULT_FOODCHAIN = fc` is similar to default parameters in Flask. It does not make sense to pass it everytime.

>`CODE != TUTORIAL`

<br>

We can go step further and modify FoodChain class:
- new parameter in constructor
- last 4 lines

```
    @classmethod
    def from_file(cls, filepath, as_default=False):
        with open(filepath, 'rt') as file:
            lines = file.readlines()
        pairs = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            left, right = line.split(' eats ')
            pairs.append((left.strip(), right.strip()))
        foodchain = cls(pairs)
        if as_default:
            Entity.DEFAULT_FOODCHAIN = foodchain
        return foodchain
```

But know Foodchain knows about Entity before it actually exists:

```
fc = FoodChain.from_file('app/foodchain.txt', as_default=True)
>>> bear = Entity('bear')
>>> cow = Entity('cow')
>>> print(bear.eats(cow))
True
```

## 5. Connecting objects
<hr>
When trying to connect 2 objects like above, you can do it in one of them or out of them. Separation is not always good.