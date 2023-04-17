from rich import *
from caracter import Character
from art import *
from screen import *
import random

def ajouter_caracteristique(self, p_caracteristiques):
    while p_caracteristiques > 0:
        print(f"Vous avez obtenu {p_caracteristiques} points de caractéristiques !")
        print(f"Statistiques actuelles :\n(ATK : {character.attack_value} ⚔️ / DEF : {character.defense_value}🛡️ / VIT : {character.vitesse}⚡️)\n")
        print(f"[italic]Vous avez {p_caracteristiques} points de caractéristique à attribuer :[italic]")


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

        self.max_health += n_hp
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

            self.attack_value += n_atk
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

            self.defense_value += n_def
            p_caracteristiques -= n_def

def ajouter_or(self, quantite_or):
        """ Ajoute de l'or à l'inventaire du personnage """
        self.gold += quantite_or
        print(f"[yellow]{self.name} a trouvé {quantite_or} pièces d'or ![yellow]")

def ajouter_arme(self, arme):
        """ Ajoute une arme à l'inventaire du personnage """
        self.armes.append(arme)
        print(f"{self.name} a ajouté {arme} à son inventaire.")

def ajouter_armure(self, armure):
    """ Ajoute une armure à l'inventaire du personnage """
    self.armures.append(armure)
    print(f"{self.name} a ajouté {armure} à son inventaire.")

def ajouter_potion(self, potion):
    """ Ajoute une potion à l'inventaire du personnage """
    self.potions.append(potion)
    print(f"[purple]{self.name} a trouvé une {potion} ![/purple]")

def ajouter_xp(self, xp):
    level_t=0
    self.p_experience += xp
    print(f"[blue]{self.name} a obtenu {xp} points d'expérience ! [blue]")
    while self.p_experience >= 10:
        self.level += 1
        level_t +=1
        self.p_experience -= 10
        sound_level_up()
        wait_input()
        print(f"[blue]{self.name} a atteint le niveau {self.level} ![blue]")

    ajouter_caracteristique(self, level_t)

def afficher_inventaire(self):
    """ Affiche l'inventaire complet du personnage """
    os.system("cls")
    tprint(f"INVENTAIRE DE  {self.name}:")
    print(f"- Or: {self.gold}")
    print("- Armes: ")
    for arme in self.armes:
        print(f"  - {arme}")
    print("- Armures: ")
    for armure in self.armures:
        print(f"  - {armure}")
    wait_input()
