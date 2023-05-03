import os
from screen import *
import time
from rich import *
from random import *
from screen import Entree
from sounds import *
from art import *
from inventory import *

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
        armure_bonus = self.armures[0].bonus if len(self.armures) > 0 else 0 
        wounds = (self.compute_encaisse(roll, damages)) - armure_bonus
        if wounds < 0:
            wounds = 0
        print(f"DEFENSE🛡️\n     (Dégats: {damages} - DEF: {self.defense_value} - Armure {armure_bonus} - Dé: {roll})\n     [blue]{self.get_name()} se défend[/blue] contre {damages} dégats et en prends {wounds}.\n")
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
        return (f"Stats actuelles : {self.health} ❤️ / {self.attack_value+arme_bonus} ⚔️ / {self.defense_value+armure_bonus} 🛡️ / {self.vitesse} ⚡️\n\nStats de classe : {self.classe_health} ❤️ / {self.classe_attack} ⚔️ / {self.classe_defense} 🛡️ / {self.classe_vitesse} ⚡️\nAméliorations   : {self.carac_health} ❤️ / {self.carac_attack} ⚔️ / {self.carac_defense} 🛡️ / {self.carac_vitesse} ⚡️\nEquipement      : Ø ❤️ / {arme_bonus} ⚔️ / {armure_bonus} 🛡️ / Ø ⚡️\n")

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
        super().__init__(20, 8, 6, 5, a_dice)
    
    def compute_damages(self, roll, target):
        print("[#3498DB]Bonus : Coup critique du Warrior ! (+2 damages)[#3498DB]")
        return super().compute_damages(roll, target) + 2
    
    def bonus_classe_print(slef):
        return f"[#3498DB](Bonus : +2 ATK par tour !)[#3498DB]"
    
    def bonus_arme_print(self):
        return f"Cette classe utilise des épées"

class Mage(Character):
    type = "Mage"

    def __init__(self):
        super().__init__(17, 6, 9, 7, a_dice)

    def compute_damages(self, roll, target):
        if self.health == self.max_health:
            print("[#3498DB]Bonus : Pas de soin ! (vie max) ![#3498DB]")
        else:
            print("[#3498DB]Bonus : Soin du mage ! (+ 1 HP)[#3498DB]")
            self.health +=1
        return super().compute_damages(roll, target)
    
    def bonus_classe_print(self):
        return f"[#3498DB](Bonus : +1 HP par tour !)[#3498DB]"
    
    def bonus_arme_print(self):
        return f"Cette classe utilise des sceptres"

class Thief(Character):
    type = "Voleur"
    def __init__(self):
        super().__init__(18, 8, 6, 10, a_dice)

    def bonus_classe_print(self):
        return f"[#3498DB](Bonus : x2,5 or (arrondi au sup.) par combat !)[#3498DB]"
    
    def bonus_arme_print(self):
        return f"Cette classe utilise des dagues"

class Looser(Character):
    type = "Looser"

    def __init__(self):
        super().__init__(1, 1, 1, 1, a_dice)

w = Warrior()
m = Mage()
t = Thief()
l = Looser()

classes = [w, m, t]
   
def create_character():
    os.system("cls")
    tprint("CREATION DE PERSONNAGE")
    name = Entree("Le nom de votre personnage ?","> ", True).run()
    #valid_inputs = ["1", "2", "3", "4"]
    
    while True:
        try:
            tprint("CREATION DE PERSONNAGE")
            print(f"[pink]{name}[pink], choisissez votre classe (HP ❤️ / ATK ⚔️ / DEF 🛡️ / VIT ⚡️) : \n")
            ct = 0
            for classe in classes:
                ct += 1
                print(f"{ct}. {classe.stats_print()}")
                print("    " + classe.bonus_classe_print())
                print("    " + classe.bonus_arme_print()+ "\n")

            # Loop until a valid integer is entered
            while True:
                classe_choix_str = Entree("Saisissez le numéro associé a la classe...", "> ").run()
                if classe_choix_str.isdigit():
                    classe_choix = int(classe_choix_str)
                    if 1 <= classe_choix <= len(classes):
                        break
                print(f"[italic][red]Veuillez saisir une valeur entre 1 et 3 ![red][italic]\n")

            selected_class = classes[classe_choix-1]
            character = selected_class
            character.name = name
            # exit the loop once a valid class index is entered

        except ValueError:
            tprint("CREATION DE PERSONNAGE")
            os.system("cls")
            print(f"[italic][red]Veuillez saisir une valeur entre 1 et 3 ![red][italic]\n")
        
        p_caracteristiques=10

        while p_caracteristiques > 0:
            os.system("cls")
            tprint("STATS DE PERSONNAGE")
            print("Bonjour " + Character.get_name(character) + " le " + Character.get_type(character) + "!\n")
            print("Statistiques actuelles : \n" + character.stats_print_carac())
            print(f"[italic]Vous avez {p_caracteristiques} points de caractéristique à attribuer : (Entre 0 pour passer à la statistique suivante)[italic]\n")

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
                        n_atk = int(Entree(f"\nCombien de points d'ATK ⚔️ ? (maximum {max_atk_points}): ", "> ").run())
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
                        n_def = int(Entree(f"\nCombien de points de DEF 🛡️ ? (maximum {max_def_points}): ", "> ").run())
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
        return(f"HP : {self.max_health} ❤️ / ATK : {self.attack_value} ⚔️ / DEF : {self.defense_value}🛡️ / VIT : {self.vitesse}⚡️\n")

    def encaisse(self, damages):
        roll = self.dice.roll()
        wounds = (self.compute_encaisse(roll, damages))
        if wounds < 0:
            wounds = 0
        print(f"DEFENSE🛡️\n     (Dégats: {damages} - DEF: {self.defense_value} - Dé: {roll})\n     [blue]{self.get_name()} se défend[/blue] contre {damages} dégats et en prends {wounds}.\n")
        self.decrease_health(wounds)
        self.show_health()

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
        super().__init__("Gobelin",12, 6, 5, 6, a_dice)
class Squelette(Enemy):
    def __init__(self):
        super().__init__("Squelette",12, 7, 4, 8, a_dice)
class Ogre(Enemy):
    def __init__(self):
        super().__init__("Ogre",15, 12, 7, 4, a_dice)
class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie",10, 7, 5, 4, a_dice)
class Golem(Enemy):
    def __init__(self):
        super().__init__("Golem",15, 10, 8, 4, a_dice)
class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 15, 12, 6, 6, a_dice)       
class Fantome(Enemy):
    def __init__(self):
        super().__init__("Fantome", 12, 10, 4, 8, a_dice)
class Geant(Enemy):
    def __init__(self):
        super().__init__("Géant", 15, 12, 7, 4, a_dice) 
class Minotaure(Enemy):
    def __init__(self):
        super().__init__("Minautaure", 10, 12, 7, 8, a_dice)

#boss
class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon",40, 20, 15, 8, a_dice)
class Hydre(Enemy):
    def __init__(self):
        super().__init__("Hydre", 50, 15, 20, 11, a_dice)
class Kraken(Enemy):
    def __init__(self):
        super().__init__("Kraken",60, 25, 10, 0, a_dice)

gobelin = Gobelin()
squelette = Squelette()
ogre = Ogre()
zombie = Zombie()
golem = Golem()
troll = Troll()
fantome = Fantome()
geant = Geant()
minautaure = Minotaure()

dragon = Dragon()
kraken = Kraken()
hydre = Hydre()

enemies = [gobelin, squelette, ogre, zombie, golem, troll, fantome, geant, minautaure]
boss = [dragon, kraken, hydre]

def random_enemy():
    return choice(enemies)

def random_boss():
    return choice(boss)
