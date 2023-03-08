from classes.character import Character
from classes.weapon import Weapon
import random

class Ninja(Character):

    def __init__(self, name):
        super().__init__(name)
        self.strength = 85
        self.weapon = Weapon("Katana")

    def regular_attack(self,target):
        super().attack(target)
    
    def special_attack(self, target):
        target.health -= (self.strength + (self.dex-100))
        print(f"Shuriken throw hits {target.name} for {(self.strength + (self.dex-100))} damage and has {target.health}HP remaining\n")

    def reaction(self, enemy):
        random_chance = random.randint(0,2)

        if random_chance == 0:
            print(f"{self.name} deftly dodged the attack and took no damage\n")
            return self
        else: 
            enemy.regular_attack(self)
            