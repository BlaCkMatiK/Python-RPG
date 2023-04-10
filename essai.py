from dice import Dice
import os
class Character:
    type = "character"

    def __init__(self, max_health, attack, defense, vitesse, dice):
        self.name = ""
        self.max_health = max_health
        self.health = self.max_health
        self.attack_value = attack
        self.defense_value = defense
        self.dice = dice
        self.status = "normal"
        self.discrétion = 5
        self.vitesse = vitesse
        self.vitesse_T = 0
        self.gold = 0
        self.armures = []
        self.armes = []
        self.potions = [] 

    def get_name(self):
        return self.name

    def show_health(self):
        missing_health = self.max_health - self.health
        health_bar = f"{self.name} healthbar : [{'●'*self.health}{'○'*missing_health}] {self.health}/{self.max_health}hp\n"
        print(health_bar)

def create_character():
    a_dice=Dice(6)
    name = input("Nom ? : \n")
    # job = input("What is your job? ")
    # strength = int(input("What is your strength level (1-10)? "))
    # dexterity = int(input("What is your dexterity level (1-10)? "))
    # intelligence = int(input("What is your intelligence level (1-10)? "))
    character = Character(10,10,10,10,a_dice)
    character.name = name
    print("Hello, " + Character.get_name(character) + "!")

    return character

def stats(self):
    print(f"{Character.get_name(self)}, {Character.show_health(self)}")

def main():
    os.system("cls")
    player = create_character()
    stats(player)

if __name__ == "__main__":
    main()
    