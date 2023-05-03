from rich import *
from caracter import *
from art import *
from screen import *
from sounds import *
import os

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
                    n_hp = int(Entree(f"\nCombien de points d'HP ? (maximum {max_hp_points}): ", "> ").run())
                    if 0 <= n_hp <= max_hp_points:
                        break
                    else:
                        print(f"Entrez une valeur entre 0 et {max_hp_points}")
                except ValueError:
                    os.system("cls")
                    print("Entrez un nombre entier valide")

                player.max_health += n_hp
                player.health += n_hp
                player.carac_health += n_hp
                p_caracteristiques -= n_hp

            if p_caracteristiques > 0:
                max_atk_points = min(p_caracteristiques, 10)
                while True:
                    try:
                        n_atk = int(Entree(f"Combien de points d'ATK ? (maximum {max_atk_points}): ", "> ").run())
                        if 0 <= n_atk <= max_atk_points:
                            break
                        else:
                            print(f"Entrez une valeur entre 0 et {max_atk_points}")
                    except ValueError:
                        os.system("cls")
                        print("Entrez un nombre entier valide")

                    player.attack_value += n_atk
                    player.carac_attack += n_hp
                    p_caracteristiques -= n_atk

            if p_caracteristiques > 0:
                max_def_points = min(p_caracteristiques, 10)
                while True:
                    try:
                        n_def = int(Entree(f"Combien de points de DEF ? (maximum {max_def_points}): ", "> ").run())
                        if 0 <= n_def <= max_def_points:
                            break
                        else:
                            print(f"Entrez une valeur entre 0 et {max_def_points}")
                    except ValueError:
                        os.system("cls")
                        print("Entrez un nombre entier valide")

                    player.defense_value += n_def
                    player.carac_defense += n_hp
                    p_caracteristiques -= n_def

    def ajouter_xp(self, player, xp):
        level_t=0
        player.p_experience += xp
        print(f"[blue]{player.name} a obtenu {xp} points d'expérience ! [blue]")
        while player.p_experience >= 10:
            player.level += 1
            level_t +=1
            player.p_experience -= 10
            Entree("", ">", False).run()
            sound_level_up()
            tprint("LEVEL UP !")
            print(f"[blue]{player.name} a atteint le niveau {player.level} ![blue]")

        self.ajouter_caracteristique(player, level_t)

    def ajouter_potion(self, player, potion):
        sound_item()
        player.potions.append(potion)

    def ajouter_arme(self, player, arme):
        if player.type == arme.classe:
            arme.bonus *=2
        if player.armes == []:
            player.armes.append(arme)
        else :
            print(f"Vous posez votre {player.armes[0].name} !")
            player.armes = []
            player.armes.append(arme)
        sound_item()

    def ajouter_armure(self, player, armure):
        if player.armures == []:
            player.armures.append(armure)
        else :
            print(f"Vous posez votre {player.armures[0].name} !")
            player.armures = []
            player.armures.append(armure)
        sound_item()

    def afficher_inventaire(self, player):
        tprint(f"INVENTAIRE DE  {player.name}:")
        print(f"[yellow]Pièces d'or: {player.gold}[yellow]\n")
        print("[#82E0AA]Armes ⚔️ : [#82E0AA]")
        if player.armes == []:
            print("    [italic][red]Vous ne possédez aucune arme[red][italic]\n")
        else:    
            for arme in player.armes:
                if player.type == arme.classe:
                    print(f"    - {str(arme)} / [blue]Arme de classe : BONUS x2 !\n")
                    
                else:
                    print(f"    - {str(arme)}\n")
        print("[#82E0AA]Armures 🛡️ : [#82E0AA]")
        if player.armures == []:
            print("    [italic][red]Vous ne possédez aucune armure[red][italic]\n")
        else:    
            for armure in player.armures:
                print(f"  - {str(armure)}\n")
        print("[#82E0AA]Potions ❤️ : [#82E0AA]")
        if player.potions == []:
            print("     [italic][red]Vous ne possédez aucune potion[red][italic]\n")
        else:    
            for potion in player.potions:
                print(f"  - {str(potion)}")
        Entree(f"[italic]Appuez sur Entrée pour continuer ... [italic]", "", True).run()

    def ajouter_hp(self, player, potion):
        if player.health + potion.bonus > player.max_health:
            potion.bonus = player.max_health - player.health
        player.health += potion.bonus
        sound_heal()
        time.sleep(3)

    def achat(self, player, objet):
        if player.gold >= objet.price:
            player.gold -= objet.price
            if objet.type=="arme":
                self.ajouter_arme(player, objet)
            elif objet.type=="armure":
                self.ajouter_armure(player, objet)
            else:
                self.ajouter_potion(player, objet)
            print(f"Vous achetez {objet.name} pour [yellow]{objet.price} or[yellow] !\nIl vous reste [yellow]{player.gold} or[yellow] !")
            sound_item()
        else:
            Entree("[red]Hé ! Vous n'avez pas assez d'argent pour acheter cet objet ![red]", "> ").run()