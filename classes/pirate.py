from classes.character import Character
from classes.weapon import Weapon
import random

class Pirate(Character):

    def __init__(self, name):
        super().__init__(name)
        self.speed = 85
        self.health = 650
        self.dex = 100
        self.weapon = Weapon("Blunderbuss")

    def regular_attack(self, target):
        super().attack(target)

    def special_attack (self, target):
        target.health -= (self.strength + (self.dex-100))
        print(f"Parrot Peck hits {target.name} for {(self.strength + (self.dex-100))} damage and has {target.health}HP remaining\n")

    def reaction(self, enemy):
        random_chance = random.randint(0,3)

        if random_chance == 0:
            print(f"{self.name} blocked the attack with his sword and avoided taking damage!\n")
            return self
        else: 
            enemy.regular_attack(self)
