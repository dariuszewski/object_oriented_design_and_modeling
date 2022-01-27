from collections import defaultdict
from unittest.mock import DEFAULT
from entity import Entity

class FoodChain:
    def __init__(self, pairs):
        self.relation = defaultdict(set)
        for k, v in pairs:
            self.relation[k].add(v)

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


    def __call__(self, entity):
        class SpeciesSet(set):
            def __contains__(self, item):
                if hasattr(item, 'species'):
                    return super().__contains__(item.species)
                return super().__contains__(item)

        if entity.species in self.relation:
            return SpeciesSet(self.relation[entity.species])
        return set()


class Entity:

    DEFAULT_FOODCHAIN = None

    def __init__(self, species, foodchain):
        self.species = species
        self.foodchain = foodchain

    def eats(self, other):
        foodchain = self.foodchain or self.DEFAULT_FOODCHAIN
        return other in self.foodchain(self)



fc = FoodChain.from_file('app/foodchain.txt')

Entity.DEFAULT_FOODCHAIN = fc

fox = Entity('fox')
sheep = Entity('sheep')
fox.eats(sheep)

