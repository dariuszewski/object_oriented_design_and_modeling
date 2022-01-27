from app.chain import FoodChain
from app.entity import Entity
from itertools import product

fc = FoodChain.from_file('app/foodchain.txt', as_default=True)

def get_survivors(foodchain, animals):
    '''
    this function accepts an animal to result, checks if animal can
    eat any other animal in result, then checks if any animal in 
    result can eat current animal.
    returns survivors.
    '''
    
    entities = iter([Entity(animal) for animal in animals])
    result = []


    for animal in animals:
        predator = next(entities)

        for animal in result:
            if predator.eats(animal):
                while animal in result:
                    print(f'{predator.species} eats {animal}')
                    result.remove(animal)
            else:
                break
        result.append(predator.species)
        for animal in result:
            if Entity(animal).eats(predator.species):
                while predator.species in result:
                    print(f'{animal} eats {predator.species}')
                    result.remove(predator.species)

    print(result)


get_survivors(fc, ["bear", "fox", "chicken", "bug"])



