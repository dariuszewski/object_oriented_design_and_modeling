#from preloaded import EXPERIENCE, ROCKS
EXPERIENCE = {}
ROCKS = {}
class Miner:
    def __init__(self, xp=0):
        self.xp = xp
        self.level = 1
        for level, xp in EXPERIENCE.items():
            if self.xp >= xp:
                self.level = level
            else:
                break
            
    def mine(self, rock):
        level, xp = ROCKS[rock]
        
        if self.level >= level:        
            self.xp += xp
            
            if self.level < 40 and self.xp >= EXPERIENCE[self.level + 1]:
                self.level += 1
                return f"Congratulations, you just advanced a Mining level! Your mining level is now {self.level}."
            else:
                return "You swing your pick at the rock."
            
        else:
            return f"You need a mining level of {level} to mine {rock}."