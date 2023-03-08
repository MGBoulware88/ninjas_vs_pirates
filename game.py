from classes.character import Character
from classes.ninja import Ninja
from classes.pirate import Pirate
from classes.weapon import Weapon
import random

Ninja1 = Ninja("Michelanglo")
## method to equip a weapon
Pirate1 = Pirate("Jack Sparrow")
#  game code here

while Ninja1.health > 0 and Pirate1.health > 0:
    print(
        "Welcome to our game. We are currently testing it.\nWe are in a world where the Ninjas and Pirates are at war\nNinjas and Pirates have been sworn enemies since time immemorial\nWill you take up arms with the sneaky Ninjas or will you get down and dirty with the Pirates?\n"
        )
    
    # player chooses character
    player_character = ""
    allegiance = ""
    response = ""
    while not allegiance == "1" or not allegiance == "2":
        if response == "1":
            Ninja1.health = 500
            Pirate1.health = 650
            print("Let's play again!")
        elif response == "2":
            if Ninja1.health <= 0:
                break
            elif Pirate1.health <= 0:
                break
        
        
        allegiance = input("Choose a side: Enter 1 for Ninja or 2 for Pirate!\n")

        # print(allegiance)

        if allegiance == "1":
            player_character = Ninja1
            computer_character = Pirate1 #maybe some rand chance to get Ninja2
        elif allegiance == "2":
            player_character = Pirate1
            computer_character = Ninja1 #some rand chance to get Pirate2
        else: 
            print(allegiance)
    # player chooses actions
        response = ""
        while not response == "1" or not response == "2":
            if player_character == Ninja1:
                response = input("Nimble Ninja, what is your move?\n1 - Regular Attack\n2 - Special Attack\n3 - Help Menu\n")

                if response == "1":
                    print("Player Attack")
                    computer_character.reaction(player_character)
                    print("Enemy Attack")
                    player_character.reaction(computer_character)                   
                elif response == "2":
                    print("Player Attack")
                    player_character.special_attack(computer_character)
                    print("Enemy Attack")
                    player_character.reaction(computer_character)
                elif response == "3":
                    Character.check_info(player_character) 
            #remove else if you want to play 2 player
            else:
                response = input("Ahoy, Pirate - What be thy action?\n1 - Regular Attack\n2 - Special Attack\n3 - Help Menu\n")

                if response == "1":
                    print("Player Attack")
                    computer_character.reaction(player_character)
                    print("Enemy Attack")
                    player_character.reaction(computer_character) 
                elif response == "2":
                    print("Player Attack")
                    player_character.special_attack(computer_character)
                    print("Enemy Attack")
                    player_character.reaction(computer_character)
                elif response == "3":
                    Character.check_info(player_character)

            if computer_character.health <= 0:
                print("CONGRATULATIONS!!!")
                response = input("Would you like to play again?\n1 for Play Again\n2 for Quit\n")
                break
            elif player_character.health <= 0:
                print("GAME OVER")
                response = input("Would you like to play again?\n1 for Play Again\n2 for Quit\n")
                break