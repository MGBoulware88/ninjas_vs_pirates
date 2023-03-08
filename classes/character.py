class Character:
    def __init__(self, name):
        self.name = name
        self.strength = 120
        self.speed = 150
        self.health = 500
        self.dex = 150

    def attack (self, target):
        # use self.dex to determine if attack hits or crits
        target.health -= self.strength
        print(f"{target.name} takes {self.strength} damage and has {target.health}HP remaining\n")
        return self
       

    def check_info(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        # print() information about what the options will do
