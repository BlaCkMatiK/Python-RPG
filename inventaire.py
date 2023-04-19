from rich import *
from caracter import *
from art import *
from screen import *

class Inventaire(object):
    def __init__(self, player):
        self.player = player
    
    def ajouter_or(self, player, nb_or):
        player.gold += nb_or
        print(f"[yellow]{player.name} a trouvé {nb_or} pièces d'or ![yellow]")
    
    def ajouter_caracteristique(self, player, p_caracteristiques):
        while p_caracteristiques > 0:
            print(f"Vous avez obtenu {p_caracteristiques} points de caractéristiques !")
            print(f"Statistiques actuelles :\n(ATK : {player.attack_value} ⚔️ / DEF : {player.defense_value}🛡️ / VIT : {player.vitesse}⚡️)\n")
            print(f"[italic]Vous avez {p_caracteristiques} points de caractéristique à attribuer :[italic]")

            max_hp_points = min(p_caracteristiques, 10)
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

            player.max_health += n_hp
            player.health += n_hp
            p_caracteristiques -= n_hp

            if p_caracteristiques > 0:
                max_atk_points = min(p_caracteristiques, 10)
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

                player.attack_value += n_atk
                p_caracteristiques -= n_atk

            if p_caracteristiques > 0:
                max_def_points = min(p_caracteristiques, 10)
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

                player.defense_value += n_def
                p_caracteristiques -= n_def

    def ajouter_xp(self, player, xp):
        level_t=0
        player.p_experience += xp
        print(f"[blue]{player.name} a obtenu {xp} points d'expérience ! [blue]")
        while player.p_experience >= 10:
            player.level += 1
            level_t +=1
            player.p_experience -= 10
            wait_input()
            sound_level_up()
            tprint("LEVEL UP !")
            print(f"[blue]{player.name} a atteint le niveau {player.level} ![blue]")

        self.ajouter_caracteristique(player, level_t)

    def ajouter_potion(self, player, potion):
        player.potions.append(potion)
        print(f"Vous obtenez une {potion.name}")

    def ajouter_arme(self, player, arme):
        if player.armes == []:
            player.armes.append(arme)
            print(f"Vous obtenez une {arme.name}")
        else :
            print("Vous avez déja une arme !")

    def ajouter_armure(self, player, armure):
        if player.armures == []:
            player.armures.append(armure)
            print(f"Vous obtenez une {armure.name}")
        else :
            print("Vous avez déja une arme !")

    def afficher_inventaire(self, player):
        tprint(f"INVENTAIRE DE  {player.name}:")
        print(f"- Or: {player.gold}")
        print("- Armes: ")
        if player.armes == []:
            print("    Aucune arme")
        else:    
            for arme in player.armes:
                print(f"  - {str(arme)}")
        print("- Armures: ")
        if player.armures == []:
            print("    Aucune armure")
        else:    
            for armure in player.armures:
                print(f"  - {str(armure)}")
        print("- Potions: ")
        if player.potions == []:
            print("     Aucune potion")
        else:    
            for potion in player.potions:
                print(f"  - {str(potion)}")
        #wait_input()

    def ajouter_hp(self, player, potion):
        if (player.max_health - potion.bonus) > player.health :
            player.health += potion.bonus
        else :
            pass

# def ajouter_caracteristique(self, p_caracteristiques):
#     while p_caracteristiques > 0:
#         print(f"Vous avez obtenu {p_caracteristiques} points de caractéristiques !")
#         print(f"Statistiques actuelles :\n(ATK : {self.attack_value} ⚔️ / DEF : {self.defense_value}🛡️ / VIT : {self.vitesse}⚡️)\n")
#         print(f"[italic]Vous avez {p_caracteristiques} points de caractéristique à attribuer :[italic]")

#         max_hp_points = min(p_caracteristiques, 10)
#         while True:
#             try:
#                 n_hp = int(input(f"\nCombien de points d'HP ? (maximum {max_hp_points}): "))
#                 if 0 <= n_hp <= max_hp_points:
#                     break
#                 else:
#                     print(f"Entrez une valeur entre 0 et {max_hp_points}")
#             except ValueError:
#                 os.system("cls")
#                 print("Entrez un nombre entier valide")

#         self.max_health += n_hp
#         p_caracteristiques -= n_hp

#         if p_caracteristiques > 0:
#             max_atk_points = min(p_caracteristiques, 10)
#             while True:
#                 try:
#                     n_atk = int(input(f"Combien de points d'ATK ? (maximum {max_atk_points}): "))
#                     if 0 <= n_atk <= max_atk_points:
#                         break
#                     else:
#                         print(f"Entrez une valeur entre 0 et {max_atk_points}")
#                 except ValueError:
#                     os.system("cls")
#                     print("Entrez un nombre entier valide")

#             self.attack_value += n_atk
#             p_caracteristiques -= n_atk

#         if p_caracteristiques > 0:
#             max_def_points = min(p_caracteristiques, 10)
#             while True:
#                 try:
#                     n_def = int(input(f"Combien de points de DEF ? (maximum {max_def_points}): "))
#                     if 0 <= n_def <= max_def_points:
#                         break
#                     else:
#                         print(f"Entrez une valeur entre 0 et {max_def_points}")
#                 except ValueError:
#                     os.system("cls")
#                     print("Entrez un nombre entier valide")

#             self.defense_value += n_def
#             p_caracteristiques -= n_def

# def ajouter_or(self, quantite_or):
#         """ Ajoute de l'or à l'inventaire du personnage """
#         self.gold += quantite_or
#         print(f"[yellow]{self.name} a trouvé {quantite_or} pièces d'or ![yellow]")

# def ajouter_arme(self, arme):
#         """ Ajoute une arme à l'inventaire du personnage """
#         self.armes.append(arme)
#         print(f"{self.name} a ajouté {arme} à son inventaire.")

# def ajouter_armure(self, armure):
#     """ Ajoute une armure à l'inventaire du personnage """
#     self.armures.append(armure)
#     print(f"{self.name} a ajouté {armure} à son inventaire.")

# def ajouter_potion(self, potion):
#     """ Ajoute une potion à l'inventaire du personnage """
#     self.potions.append(potion)
#     print(f"[purple]{self.name} a trouvé une {potion} ![/purple]")

# def ajouter_xp(self, xp):
#     level_t=0
#     self.p_experience += xp
#     print(f"[blue]{self.name} a obtenu {xp} points d'expérience ! [blue]")
#     while self.p_experience >= 10:
#         self.level += 1
#         level_t +=1
#         self.p_experience -= 10
#         wait_input()
#         sound_level_up()
#         tprint("LEVEL UP !")
#         print(f"[blue]{self.name} a atteint le niveau {self.level} ![blue]")

#     ajouter_caracteristique(self, level_t)

# def afficher_inventaire(self):
#     """ Affiche l'inventaire complet du personnage """
#     os.system("cls")
#     tprint(f"INVENTAIRE DE  {self.name}:")
#     print(f"- Or: {self.gold}")
#     print("- Armes: ")
#     for arme in self.armes:
#         print(f"  - {arme}")
#     print("- Armures: ")
#     for armure in self.armures:
#         print(f"  - {armure}")
#     wait_input()
