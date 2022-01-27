from app.chain import FoodChain
from app.entity import Entity

fc = FoodChain.from_file('app/foodchain.txt', as_default=True)

fox = Entity('fox')
sheep = Entity('sheep')
grass = Entity('grass')
print(sheep in fc(fox))
print(fox.eats(sheep))

eaters = [fox, sheep]
foods = [sheep, grass]
matches = map(Entity.eats, eaters, foods)
print(*matches)

bear = Entity('bear')
cow = Entity('cow')
print(bear.eats(cow))
