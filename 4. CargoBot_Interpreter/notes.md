# LAB4 CargoBot

## 1. Levels of understanding models
<hr>

>During modelling classes we can think of their names as of physical objects they represent, but we can also take a different approach and think of logical elements of program. 


In the CargoBot interpreter we can think of crates as Stacks and try to implment it as follows:

```
class Stack(list):
    def push(self, item):
        return append(item)
    def peek(self):
        return self[-1]
    def pop(self):
    return super().pop()
```

<b>BUT  it breaks Liskov rule of OOP, we implement a class which does not extend it's parent, but restricts it !</b>

We end up with an adapter which just changes names of functions ...

## 2. `ProgramControl` class
<hr>

- responsible for storing information about state of the program (memory)

- delivering commands

```
class ProgramControl:

    def __init__(self, programs):
        self.programs = programs
```

this is already problematic. we referencing something what can be mutatable. 

- we should check pre-conditions just before calling methods or we don't care at all. 

- we can validate right after start of the function, but we have to take care of keeping polymorphism: 

```
class ProgramControl:

    def __init__(self, programs):
        if not isinstance(programs, list):
            raise TypeError
        self.programs = programs

        self.current_instruction = (0, 0)
```
 - The problem here is that a simple tuple will not pass the text.
 -  The class is not really autonomic as it depends from input. 
 - we have additional problem, the class have both, provided and not provided attrs. It is a dangerous situation as cen lead to destnchronization

 Finally we implement:

 ```
class ProgramControl:

    def __init__(self, programs):
        self.programs = [list(p) for p in programs]
        self.current_instruction = (0, 0)
 ```

 advantages
 - we don't copy reference
 - we don't care what is `programs`
 - we have iterable for sure
 - we have validation and protection from outside in one line

 ## 2. `ProgramControl` - jumping and ending
 <hr>

