
class Entity:

    DEFAULT_FOODCHAIN = None

    def __init__(self, species, foodchain=None):
        self.species = species
        self.foodchain = foodchain

    def eats(self, other):
        foodchain = self.foodchain or self.DEFAULT_FOODCHAIN
        return other in foodchain(self)