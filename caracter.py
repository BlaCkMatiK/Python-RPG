import os
import random
import time
from rich import print
from random import *

from dice import Dice, RiggedDice

a_dice=Dice(6)

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

    def __str__(self):
        return f"{self.name} le {type(self).type} démmare le combat avec {self.max_health}hp ({self.attack_value} atk / {self.defense_value} def)\n"

    def regenerate(self):
        self.health = self.max_health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        print("[",end="")
        if self.health / self.max_health >= 0.5:
            emoji = "💚"
        else :
            emoji = "❤️"
        for i in range(0, self.health):
            print(emoji,end="")
        for i in range(self.health, self.max_health):
            print("🖤", end="")
        print("]")

    # def show_health(self):
    #     missing_health = self.max_health - self.health
    #     health_bar = f"Barre de vie de {self.name} : [{'●'*self.health}{'○'*missing_health}] {self.health}/{self.max_health}hp\n"
    #     print(health_bar)

    def get_type(self):
        return type(self).type

    def get_defense(self):
        return self.defense_value

    def get_name(self):
        return self.name

    def compute_damages(self, roll, target):
        damages = roll + self.attack_value
        return damages

    def attack(self, target):
        if self.is_alive():

            roll = self.dice.roll()
            damages = self.compute_damages(roll, target)
            print(f"⚔️ [red]{self.get_name()} attaque[/red] avec {damages} dommages (attack: {self.attack_value} + dé {roll})")
            target.defend(damages)

    def compute_defense(self, roll, damages):
        return damages - roll - self.defense_value

    def defend(self, damages):
        roll = self.dice.roll()
        wounds = self.compute_defense(roll, damages)
        print(f"🛡️ [blue]{self.get_name()} se défend[/blue] contre {damages} dommages et en prends {wounds}. ({damages} dommages - défense {self.defense_value} - dé {roll})")
        if wounds < 0:
            wounds = 0
        self.decrease_health(wounds)
        self.show_health()

def create_character():
    name = input("Le nom de votre personnage ? :  ")
    classe = input("Choisis ta classe (hp / atk / def / vit): \n 1. Warrior (20 / 8 / 5 / 2) \n 2. Mage (15 / 10 / 10 / 2) \n 3. Thief (10 / 10 / 10 / 10) \n:")
    # while classe == 0 or (classe != 1 and classe != 2) :
    #     classe = input("Choisis ta classe : \n 1. Warrior \n 2. Mage : ")
    if classe == "1":
        character = Warrior(20, 8, 5, 2, a_dice)
    elif classe == "2":
        character = Mage(15, 10, 10, 2, a_dice)
    elif classe == "3":
        character = Thief(10,10,10,10, a_dice)
    character.name = name
    print("Hello, " + Character.get_name(character) + "!")
    
    points_de_competences = 10
    print("Vous avez", points_de_competences, "points de compétences à attribuer.")

    while points_de_competences > 0:
        print("Statistiques actuelles :")
        print("Points de vie :", character.max_health)
        print("Attaque :", character.attack_value)
        print("Défense :", character.defense_value)
        
        # Request input for HP points
        max_hp_points = min(points_de_competences, 10)  # Set maximum number of points to 10 or remaining points
        n_hp = int(input(f"Combien de points d'HP ? (maximum {max_hp_points}): "))
        while n_hp > max_hp_points:
            n_hp = int(input(f"Combien de points d'HP ? (maximum {max_hp_points}): "))
        character.max_health += n_hp
        character.regenerate()
        points_de_competences -= n_hp
        
        if points_de_competences > 0:
            # Request input for ATK points
            max_atk_points = min(points_de_competences, 10)  # Set maximum number of points to 10 or remaining points
            n_atk = int(input(f"Combien de points d'ATK ? (maximum {max_atk_points}): "))
            while n_atk > max_atk_points:
                n_atk = int(input(f"Combien de points d'ATK ? (maximum {max_atk_points}): "))
            character.attack_value += n_atk
            points_de_competences -= n_atk
            
        if points_de_competences > 0:
            # Request input for DEF points
            max_def_points = min(points_de_competences, 10)  # Set maximum number of points to 10 or remaining points
            n_def = int(input(f"Combien de points de DEF ? (maximum {max_def_points}): "))
            while n_def > max_def_points:
                n_def = int(input(f"Combien de points de DEF ? (maximum {max_def_points}): "))
            character.defense_value += n_def
            points_de_competences -= n_def
        print(character)
        print("%s entre dans une cave sombre, à la recherche de l'aventure..." % character.name)

        return character

def stats(character):
    print("TEST")
    print(f"{character.get_name()}, {character.show_health()}") 

class Warrior(Character):
    type = "Warrior"

    def compute_damages(self, roll, target):
        print("Bonus : Axe in your face ! (+3 damages)")
        return super().compute_damages(roll, target) + 3

class Mage(Character):
    type = "Mage"

    def compute_defense(self, roll, damages):
        print("Bonus : Magic armor ! (-3 wournds)")
        return super().compute_defense(roll, damages) - 3

class Thief(Character):
    type = "Thief"

    def compute_damages(self, roll, target):
        print(f"Bonus : Backstab ! (+{target.get_defense()} damages)")
        return super().compute_damages(roll, target) + target.get_defense()

class Enemy(Character):
    type = "enemy"
    def __init__(self, name, max_health, attack, defense, vitesse, dice):
        super().__init__(max_health, attack, defense, vitesse, dice)
        self.name = name

class CrawlingVermin(Enemy):
    def __init__(self):
        super().__init__("CrawlingVermin",10, 2, 1, 3, a_dice)

class ShadowStalker(Enemy):
    def __init__(self):
        super().__init__("ShadowStalker",15, 3, 2, 4, a_dice)

class VenomousSerpent(Enemy):
    def __init__(self):
        super().__init__("VenomousSerpent",20, 4, 3, 5, a_dice)

class DeathbringerScorpion(Enemy):
    def __init__(self):
        super().__init__("DeathbringerScorpion",25, 5, 4, 6, a_dice)

class AbyssalHorror(Enemy):
    def __init__(self):
        super().__init__("AbyssalHorror",30, 6, 5, 7, a_dice)


if __name__ == "__main__":
    a_dice = Dice(6)

    name = input("Le nom de votre personnage ? :  ")
    classe = input("Choisis ta classe : \n 1. Warrior \n 2. Mage \n: ")

    # while classe == 0 or (classe != 1 and classe != 2) :
    #     classe = input("Choisis ta classe : \n 1. Warrior \n 2. Mage : ")
    if classe == "1":
        character = Warrior(20, 8, 5, 2, a_dice)
    elif classe == "2":
        character = Mage(15, 10, 10, 2, a_dice)

    character.name = name
    points_de_competences = 50

    print("Vous avez", points_de_competences,
          "points de compétences à attribuer.")

    while points_de_competences > 0:
        print("Statistiques actuelles :")
        print("Points de vie :", character.max_health)
        print("Attaque :", character.attack_value)
        print("Défense :", character.defense_value)
        n_hp = int(input("Combien de points d'HP ? : "))
        character.max_health += n_hp
        character.regenerate()
        points_de_competences -= n_hp
        if points_de_competences > 0:
            n_atk = int(input("Combien de points d'ATK ? : "))
            character.attack_value += n_atk
            points_de_competences -= n_atk
            if points_de_competences > 0:
                n_def = int(input("Combien de points de DEF ? : "))
                character.defense_value += n_def
                points_de_competences -= n_def
    print(character)
    print("%s enters a dark cave, searching for adventure." % character.name)

