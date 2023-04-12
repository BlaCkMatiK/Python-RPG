import os
import random
import time
from rich import print
from random import *

from dice import Dice, RiggedDice


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
        return f"{self.name} the {type(self).type} is starting the fight with {self.max_health}hp ({self.attack_value} atk / {self.defense_value} def)\n"

    def regenerate(self):
        self.health = self.max_health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        missing_health = self.max_health - self.health
        health_bar = f"Barre de vie de {self.name} : [{'●'*self.health}{'○'*missing_health}] {self.health}/{self.max_health}hp\n"
        print(health_bar)

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
            print(
                f"⚔️ [red]{self.get_type()} {self.name} attack[/red] with {damages} damages (attack: {self.attack_value} + roll: {roll})")
            target.defend(damages)

    def compute_defense(self, roll, damages):
        return damages - roll - self.defense_value

    def defend(self, damages):
        roll = self.dice.roll()
        wounds = self.compute_defense(roll, damages)
        print(f"🛡️ [blue]{self.get_type()} {self.name} defend[/blue] against {damages} damages and take {wounds} wounds ({damages} damages - defense {self.defense_value} - roll {roll})")
        if wounds < 0:
            wounds = 0
        self.decrease_health(wounds)
        self.show_health()


def create_character():
    a_dice=Dice(6)
    name = input("Le nom de votre personnage ? :  ")
    classe = input("Choisis ta classe : \n 1. Warrior \n 2. Mage \n 3. Thief \n:")
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


class Enemy(Character):
    type = "Ennemy"


class Thief(Character):
    type = "Thief"

    def compute_damages(self, roll, target):
        print(f"Bonus : Backstab ! (+{target.get_defense()} damages)")
        return super().compute_damages(roll, target) + target.get_defense()


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

