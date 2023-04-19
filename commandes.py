import random
from caracter import *
from numpy.random import choice
from screen import *
from evenement import Event
import art
import os
from sounds import *
from inventaire import *
from items import *

class Commandes:
    def __init__(self, player, equip):
        self.player = player
        self.equip = equip

    def choix(self, player, equip):
        choix_list = {       
        "stats": self.stats,
        "explore": self.explore,
        "fuite": self.fuite,
        "combat": self.combat,
        "inventaire": self.inventaire,
        "loose": self.loose,
        "konami": self.konami,
        "quit": self.quit, 
        "heal": self.heal,
        "coffre": self.coffre,
        "marchand": self.marchand
        }

        while player.is_alive():
            tprint("COMMANDE :")
            commandFound = False
            line = Entree("[italic]Entrez une commande[italic]", ">> ", True).run()
            if line.strip():
                if line == "help":
                    self.help()
                else: 
                    for a in choix_list.keys():
                        if line.strip() == a:
                            choix_list[a](player, equip)
                            commandFound = True
                            break
                    if not commandFound:
                        os.system("cls")
                        print(f"[italic][red]{player.name} ne comprend pas ![red][italic]")
            else:
                os.system("cls")
                print(f"[italic][red]Entrez une commande ![red][italic]")
        os.system("cls")
        print(f"[red]{player.name} n'a plus de vie ![red]")
        time.sleep(2)
        quit_pygame()
        sound_game_over()
        print_game_over()
        end_stats(player)


    def stats(self, player, equip):
        player.stats()

    def help(self):
        os.system("cls")
        tprint("PAGE D'AIDE")
        print("[#D2B4DE]help[#D2B4DE]"" pour voir cette page\n""[#D2B4DE]stats[#D2B4DE]"" pour afficher les statistiques\n""[#D2B4DE]inventaire[#D2B4DE]"" pour ouvrir l'inventaire[italic]\n")
        print("[italic][#D2B4DE]explore[#D2B4DE] pour avancer\n[italic]\nVous pouvez tomber sur les évenements suivants :[#7FB3D5]\n\n -Combat (40%)\n[italic]    lorsqu'un combat est lancé, vous pouvez essayer de fuire avec [#D2B4DE]fuite[#D2B4DE]\n\n -Coffre (20%)[#ABEBC6]\n    -Arme (augmente l'ATK)\n    -Armure(augmente la DEF)\n    -Potion (soigne les HP)[#ABEBC6][italic]\n\n -Salle vide (10%)\n\n -Piege (10%)\n\n -Marchand (10%)\n     Les marchands vendent tout ce qui se trouve dans les coffres du donjon\n\n -Couloir secret (10%)\n    -Boss\n    -Coffre\n    -Marchand[#7FB3D5]")
        print("\n[#F9E79F]Attention ! Vous ne pouvez porter qu'une seule arme et qu'une seule armure à la fois !\n[italic]Prendez vous le risque de changer pour un équipement moins puissant ? :)[italic][#F9E79F]")
        Entree("\n[italic][red]Bonne chance ![red][italic]", "> ", True).run()

    def explore(self, player, equip):
        avance = Event(player, equip)
        avance.explore(player, equip)
    
    def fuite(self, player, equip):
        Entree("Fuite", "> ", True).run()
    
    def combat(self, player, equip):
        Entree("Combat", "> ", True).run()
    
    def inventaire(self, player, equip):
        equip.afficher_inventaire(player)
    
    def loose(self, player, equip):
        print(f"{player.health} - 10 = {player.health - 100}")
        player.health -= 100
    
    def konami(self, player, equip):
        print("konami")
        a = random_potion()
        b = random_arme()
        equip.ajouter_potion(player, a)
        equip.ajouter_arme(player, b)
        os.system("cls")
    
    def coffre(self, player, equip):
        print("coffre")
        a = Event(player, equip)
        a.salle_coffre(player, equip)
        os.system("cls")

    def marchand(self, player, equip):
        a = Event(player, equip)
        a.salle_magasin(player, equip)
        os.system("cls")

    def heal(self, player, equip):
        os.system("cls")
        tprint("HEAL")
        print(f"Vous avez {player.health} / {player.max_health} HP\n")
        if player.potions != []:
            ct = 0
            for potion in player.potions:
                ct += 1
                print(f"{ct}. {potion}\n")
            potion_choix = Entree("Quelle potion utiliser ?", "> ").run()
            try:
                potion_choix = int(potion_choix)
                potion = player.potions[potion_choix-1]
                player.potions.remove(potion)
                equip.ajouter_hp(player, potion)
                Entree(f"{potion.name} a été utilisé. Vous avez maintenant {player.health} / {player.max_health} HP.","", True).run()
            except (ValueError, IndexError):
                print("Choix invalide.")
        else:
            Entree("Malheuserement, vous n'avez aucune potion !\n[italic]Appuez sur entrée pour continuer ... [italic]", "", True).run()
    
    def quit(self, player, equip):
        print(f"{player.name} quitte le jeu !")
        exit(0)