import os
from screen import *
import time
from rich import *
from random import *
from screen import Entree
from sounds import *
from art import *
from inventaire import *

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
        self.defending = False
        self.vitesse_T = vitesse
        self.gold = 10
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
        self.classe_health = max_health
        self.classe_attack = attack
        self.classe_defense = defense
        self.classe_vitesse = vitesse
        self.p_experience = 0
        self.carac_health = 0
        self.carac_attack = 0
        self.carac_defense = 0
        self.carac_vitesse = 0
        self.max_dmg = 0
        self.max_encaisse = 0

    def __str__(self):
        return f"{self.name} le {type(self).type} descend dans le donjon avec : HP : {self.max_health} ❤️ / ATK : {self.attack_value} ⚔️ / DEF : {self.defense_value}🛡️ / VIT : {self.vitesse}⚡️)\n"

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
            arme_bonus = self.armes[0].bonus if len(self.armes) > 0 else 0
            damages = (self.compute_damages(roll, target)) + arme_bonus
            self.max_dmg = damages if self.max_dmg < damages else self.max_dmg
            print(f"ATTAQUE ⚔️\n      (ATK: {self.attack_value} + Arme: {arme_bonus} + Dé: {roll})\n      [red]{self.get_name()} attaque[/red] avec {damages} dégats ! (ATK: {self.attack_value} + Arme: {arme_bonus} + Dé: {roll})\n")
            sound_hit()
            target.encaisse(damages)

    def defendre(self):
        self.defending = True

    def compute_encaisse(self, roll, damages):
        return damages - roll - self.defense_value

    def encaisse(self, damages):
        roll = self.dice.roll()
        armure_bonus = self.armes[0].bonus if len(self.armes) > 0 else 0 
        wounds = (self.compute_encaisse(roll, damages)) - armure_bonus
        if wounds < 0:
            wounds = 0
        print(f"DEFENSE🛡️\n     (Dégats: {damages} - DEF: {self.defense_value} - Dé: {roll})\n     [blue]{self.get_name()} se défend[/blue] contre {damages} dégats et en prends {wounds}.\n")
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

    def choose_action(self):
        while True:
            action = Entree(f"{self.name}, choisis ton action du tour :\n\n  1. Attaquer \n  2. Défendre\n  3. Potions\n","> ",).run()
            if action in ["1", "2", "3"]:
                return action
            else :
                print("Action invalide.")

    def stats_print(self):
        return (f"{self.type} ({self.max_health} ❤️ / {self.attack_value} ⚔️ / {self.defense_value} 🛡️ / {self.vitesse} ⚡️)")
    
    def stats_print_carac(self):
        return (f"HP : {self.max_health} ❤️ (+{self.carac_health}) / ATK : {self.attack_value} ⚔️ (+{self.carac_attack}) / DEF : {self.defense_value} 🛡️ (+{self.carac_defense}) / VIT : {self.vitesse} ⚡️ (+{self.carac_vitesse})\n")
    
    def stats_final(self):
        arme_bonus = self.armes[0].bonus if len(self.armes) > 0 else 0
        armure_bonus = self.armures[0].bonus if len(self.armures) > 0 else 0
        return (f"Stats actuelles : {self.health} ❤️ / {self.attack_value} ⚔️ / {self.defense_value} 🛡️ / {self.vitesse} ⚡️\n\nStats de classe : {self.classe_health} ❤️ / {self.classe_attack} ⚔️ / {self.classe_defense} 🛡️ / {self.classe_vitesse} ⚡️\nAméliorations   : {self.carac_health} ❤️ / {self.carac_attack} ⚔️ / {self.carac_defense} 🛡️ / {self.carac_vitesse} ⚡️\nEquipement      : Ø ❤️ / {arme_bonus} ⚔️ / {armure_bonus} 🛡️ / Ø ⚡️\n")

    def stats(self):
        os.system("cls")
        tprint(f"STATS DE {self.name.upper()}")
        print(self.stats_final())
        print("Barre de vie :")
        self.show_health()
        self.show_xp()
        Entree("[italic]Appuez sur entrée pour continuer ... [italic]", "", True).run()

class Warrior(Character):
    type = "Warrior"
    def __init__(self):
        super().__init__(20, 8, 5, 2, a_dice)
    
    def compute_damages(self, roll, target):
        print("Bonus : Axe in your face ! (+3 damages)")
        return super().compute_damages(roll, target) + 3

class Mage(Character):
    type = "Mage"

    def __init__(self):
        super().__init__(15, 10, 10, 2, a_dice)

    def compute_defense(self, roll, damages):
        print("Bonus : Magic armor ! (-3 wournds)")
        return super().compute_defense(roll, damages) - 3

class Thief(Character):
    type = "Thief"
    def __init__(self):
        super().__init__(10, 10, 10, 10, a_dice)

    def compute_damages(self, roll, target):
        print(f"Bonus : Backstab ! (+{target.get_defense()} damages)")
        return super().compute_damages(roll, target) + target.get_defense()

class Looser(Character):
    type = "Looser"

    def __init__(self):
        super().__init__(1, 1, 1, 1, a_dice)

w = Warrior()
m = Mage()
t = Thief()
l = Looser()

classes = [w, m, t, l]
   
def create_character():
    os.system("cls")
    tprint("CREATION DE PERSONNAGE")
    name = Entree("Le nom de votre personnage ?","> ", True).run()
    #valid_inputs = ["1", "2", "3", "4"]
    os.system("cls")
    
    while True:
        try:
            tprint("CREATION DE PERSONNAGE")
            print(f"[pink]{name}[pink], choisissez votre classe (HP ❤️ / ATK ⚔️ / DEF 🛡️ / VIT ⚡️) : \n")
            ct = 0
            for classe in classes:
                ct += 1
                print(f"{ct}. {classe.stats_print()}")

            # Loop until a valid integer is entered
            while True:
                classe_choix_str = input("> ")
                if classe_choix_str.isdigit():
                    classe_choix = int(classe_choix_str)
                    if 1 <= classe_choix <= len(classes):
                        break
                print(f"[italic][red]Veuillez saisir une valeur entre 1 et 4 ![red][italic]\n")

            selected_class = classes[classe_choix-1]
            character = selected_class
            character.name = name
            # exit the loop once a valid class index is entered

        except ValueError:
            tprint("CREATION DE PERSONNAGE")
            os.system("cls")
            print(f"[italic][red]Veuillez saisir une valeur entre 1 et 4 ![red][italic]\n")





    # while True:
    #     try:
    #         tprint("CREATION DE PERSONNAGE")
    #         print(f"[pink]{name}[pink], choisissez votre classe (HP ❤️ / ATK ⚔️ / DEF 🛡️ / VIT ⚡️) : \n")
    #         ct = 0
    #         for classe in classes:
    #             ct+=1
    #             print(f"{ct}. {classe.stats_print()}")
    #         while True:
    #             classe_choix = input("> ")
    #             if classe_choix.isdigit():
    #                 classe_choix = int(classe_choix)
    #                 break
    #             else:
    #                 print("Veuillez entrer un nombre entier valide.")
                
    #             if classe_choix < 1 or classe_choix > len(classes):
    #                 raise ValueError("Veuillez saisir un nombre valide correspondant à la classe de votre choix.")

    #             selected_class = classes[classe_choix-1]
    #             character = selected_class
    #             character.name = name

        # if classe_choix < 1 or classe_choix > len(classes):
        #     raise ValueError("Veuillez saisir un nombre valide correspondant à la classe de votre choix.")

        # selected_class = classes[classe_choix-1]
        # character = selected_class
        # character.name = name
            # classe_choix = int(Entree("", "> ").run())
             #classe = Entree("\n\n*************\n\n1. " + Warrior().stats_print() +"\n    (Utilisent des épées)"+ "\n\n2. " + Mage().stats_print() +"\n    (Utilisent des sceptres)" + "\n\n3. " + Thief().stats_print() +"\n    (Utilisent des dagues)"+ "\n\n4. " + Looser().stats_print(), "> ", True).run()
            
        except ValueError:
            tprint("CREATION DE PERSONNAGE")
            os.system("cls")
            print("[italic][red]Veuillez saisir une valeur entre 1 et 4 ![red][italic]\n")
    
        os.system("cls")
        tprint("CREATION DE PERSONNAGE")
        print("Bonjour " + Character.get_name(character) + " le " + Character.get_type(character) + "!\n")
    
        p_caracteristiques=10

        while p_caracteristiques > 0:
            print("Statistiques actuelles : \n" + character.stats_print_carac())
            print(f"[italic]Vous avez {p_caracteristiques} points de caractéristique à attribuer :[italic]")

            # Request input for HP points
            max_hp_points = min(p_caracteristiques, 10)  # Set maximum number of points to 10 or remaining points
            while True:
                try:
                    n_hp = int(Entree(f"\nCombien de points d'HP ❤️ ? (maximum {max_hp_points}): ", "> " ).run())
                    if 0 <= n_hp <= max_hp_points:
                        break
                    else:
                        print(f"[italic][red]Entrez une valeur entre 0 et {max_hp_points}[red][italic]")
                except ValueError:
                    os.system("cls")
                    print("[italic][red]Entrez un nombre entier valide[red][italic]")

            character.max_health += n_hp
            character.carac_health += n_hp
            character.regenerate()
            p_caracteristiques -= n_hp

            if p_caracteristiques > 0:
                # Request input for ATK points
                max_atk_points = min(p_caracteristiques, 10)  # Set maximum number of points to 10 or remaining points
                while True:
                    try:
                        n_atk = int(Entree(f"Combien de points d'ATK ⚔️ ? (maximum {max_atk_points}): ", "> ").run())
                        if 0 <= n_atk <= max_atk_points:
                            break
                        else:
                            print(f"[italic][red]Entrez une valeur entre 0 et {max_atk_points}[red][italic]")
                    except ValueError:
                        os.system("cls")
                        print("[italic][red]Entrez un nombre entier valide[red][italic]")

                character.attack_value += n_atk
                character.carac_attack += n_atk
                p_caracteristiques -= n_atk

            if p_caracteristiques > 0:
                # Request input for DEF points
                max_def_points = min(p_caracteristiques, 10)  # Set maximum number of points to 10 or remaining points
                while True:
                    try:
                        n_def = int(Entree(f"Combien de points de DEF 🛡️ ? (maximum {max_def_points}): ", "> ").run())
                        if 0 <= n_def <= max_def_points:
                            break
                        else:
                            print(f"[italic][red]Entrez une valeur entre 0 et {max_def_points}[red][italic]")
                    except ValueError:
                        os.system("cls")
                        print("[italic][red]Entrez un nombre entier valide[red][italic]")

                character.defense_value += n_def
                character.carac_defense += n_def
                p_caracteristiques -= n_def
            os.system("cls")
            tprint("DESCENTE")
            print(character)
            print("%s entre dans une cave sombre, à la recherche de l'aventure..." % character.name)

        return character

class Enemy(Character):
    type = "enemy"
    def __init__(self, name, max_health, attack, defense, vitesse, dice):
        super().__init__(max_health, attack, defense, vitesse, dice)
        self.name = name
    
    def print_enemy(self):
        print("ATK : {self.attack_value} ⚔️ / DEF : {self.defense_value}🛡️ / VIT : {self.vitesse}⚡️\n")

    def stats(self):
        return(f"ATK : {self.attack_value} ⚔️ / DEF : {self.defense_value}🛡️ / VIT : {self.vitesse}⚡️\n")

    def choose_turn(self, target):
        choice = randint(1,3)
        if choice == "1" :
            print(f"{self.name} a choisi d'attaquer !")
            self.attack(target)
        elif choice == "2" :
            pass
        elif choice == "3" :
            pass

class Gobelin(Enemy):
    def __init__(self):
        super().__init__("Gobelin",15, 6, 6, 3, a_dice)

class Squelette(Enemy):
    def __init__(self):
        super().__init__("Squelette",10, 8, 6, 4, a_dice)

class Ogre(Enemy):
    def __init__(self):
        super().__init__("Ogre",18, 10, 6, 5, a_dice)

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 100, 10, 10, 10, a_dice)

class Kraken(Enemy):
    def __init__(self):
        super().__init__("Kraken", 100, 10, 10, 10, a_dice)

gobelin = Gobelin()
squelette = Squelette()
ogre = Ogre()
dragon = Dragon()
kraken = Kraken()

enemies = [gobelin, squelette, ogre]
boss = [dragon, kraken]

def random_enemy():
    return choice(enemies)

def random_boss():
    return choice(boss)
