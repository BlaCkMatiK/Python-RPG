import os
#from screen import *
import time
from rich import *
from random import *
from sounds import sound_hit
from art import *

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
        self.kills = 0
        self.tours_max = 0
        self.steps = 0
        self.chests = 0
        self.OHKO = 0
        self.traps = 0
        self.level = 1
        self.p_experience = 0

    def __str__(self):
        return f"{self.name} le {type(self).type} descend dans le donjon avec {self.max_health}hp, {self.attack_value} atk et {self.defense_value} def\n"

    def regenerate(self):
        self.health = self.max_health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        #print("[",end="\r")
        if self.health / self.max_health >= 0.5:
            emoji = "💚"
        else :
            emoji = "❤️"
        for i in range(0, self.health):
            print(emoji,end="")
        for i in range(self.health, self.max_health):
            print("🖤", end="")
        print(f"  ({self.health} / {self.max_health})\n")
        #wait_input()

    def show_health2(self):
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
            print(f"ATTAQUE⚔️\n     [red]{self.get_name()} attaque[/red] avec {damages} dommages (attack: {self.attack_value} + dé {roll})")
            sound_hit()
            target.defend(damages)

    def compute_defense(self, roll, damages):
        return damages - roll - self.defense_value

    def defend(self, damages):
        roll = self.dice.roll()
        wounds = self.compute_defense(roll, damages)
        if wounds < 0:
            wounds = 0
        print(f"DEFENSE🛡️\n     [blue]{self.get_name()} se défend[/blue] contre {damages} dommages et en prends {wounds}. ({damages} dommages - défense {self.defense_value} - dé {roll})", end="\n")
        if wounds < 0:
            wounds = 0
        self.decrease_health(wounds)
        self.show_health()
        #time.sleep(2)

    def show_xp(self):
        #print("[",end="\r")
        emoji = "🔵"        
        print(f"Niveau {self.level}")
        for i in range(0, self.p_experience):
            print(emoji,end="")
        for i in range(self.p_experience, 10):
            print("⚫", end="")
        print(f" ({self.p_experience} / 10)\n")

def turn():
    pass

def create_character():
    os.system("cls")
    tprint("CREATION DE PERSONNAGE")
    name = input("Le nom de votre personnage ? \n \n-> : ")
    valid_inputs = ["1", "2", "3", "4"]
    os.system("cls")
    
    while True:
        try:
            tprint("CREATION DE PERSONNAGE")
            print(f"[pink]{name}[pink], choisissez votre classe (hp ❤️ / atk ⚔️ / def 🛡️ / vit 💨): ")
            classe = input(f"\n\n*************\n\n1. Warrior (20 ❤️ / 8 ⚔️ / 5 🛡️ / 2 💨) \n\n2. Mage (15 ❤️ / 10 ⚔️ / 10 🛡️ / 2 💨) \n\n3. Thief (10 ❤️ / 10 ⚔️ / 10 🛡️ / 10 💨) \n\n4. Looser (1 ❤️ / 1 ⚔️ / 1 🛡️ / 1 💨) \n \n-> : ")
            if str(classe) not in valid_inputs:
                raise ValueError
            break
        except ValueError:
            tprint("CREATION DE PERSONNAGE")
            os.system("cls")
            print("Veuillez saisir une valeur entre 1 et 4 !\n")

    if classe == "1":
        character = Warrior(20, 8, 5, 2, a_dice)
    elif classe == "2":
        character = Mage(15, 10, 10, 2, a_dice)
    elif classe == "3":
        character = Thief(10,10,10,10, a_dice)
    elif classe == "4":
        character = Looser(1,1,1,1, a_dice)
    character.name = name
    
    os.system("cls")
    tprint("CREATION DE PERSONNAGE")
    print("Bonjour " + Character.get_name(character) + " le " + Character.get_type(character) + "!\n")
    
    p_caracteristiques=10

    while p_caracteristiques > 0:
        print("Statistiques actuelles :")
        print(" Points de vie :", character.max_health)
        print(" Attaque :", character.attack_value)
        print(" Défense :", character.defense_value)
        print("Vitesse :", character.vitesse)
        print(f"Vous avez {p_caracteristiques} points de caractéristique à attribuer :")

        # Request input for HP points
        max_hp_points = min(p_caracteristiques, 10)  # Set maximum number of points to 10 or remaining points
        while True:
            try:
                n_hp = int(input(f"\nCombien de points d'HP ? (maximum {max_hp_points}): "))
                if 0 <= n_hp <= max_hp_points:
                    break
                else:
                    print(f"Entrez une valeur entre 0 et {max_hp_points}")
            except ValueError:
                os.system("cls")
                print("Entrez un nombre entier valide")

        character.max_health += n_hp
        character.regenerate()
        p_caracteristiques -= n_hp

        if p_caracteristiques > 0:
            # Request input for ATK points
            max_atk_points = min(p_caracteristiques, 10)  # Set maximum number of points to 10 or remaining points
            while True:
                try:
                    n_atk = int(input(f"Combien de points d'ATK ? (maximum {max_atk_points}): "))
                    if 0 <= n_atk <= max_atk_points:
                        break
                    else:
                        print(f"Entrez une valeur entre 0 et {max_atk_points}")
                except ValueError:
                    os.system("cls")
                    print("Entrez un nombre entier valide")

            character.attack_value += n_atk
            p_caracteristiques -= n_atk

        if p_caracteristiques > 0:
            # Request input for DEF points
            max_def_points = min(p_caracteristiques, 10)  # Set maximum number of points to 10 or remaining points
            while True:
                try:
                    n_def = int(input(f"Combien de points de DEF ? (maximum {max_def_points}): "))
                    if 0 <= n_def <= max_def_points:
                        break
                    else:
                        print(f"Entrez une valeur entre 0 et {max_def_points}")
                except ValueError:
                    os.system("cls")
                    print("Entrez un nombre entier valide")

            character.defense_value += n_def
            p_caracteristiques -= n_def
        os.system("cls")
        tprint("SUDOQUEST")
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

class Looser(Character):
    type = "looser"

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

