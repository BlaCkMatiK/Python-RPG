import random
from caracter import *
from screen import *
from events import Event
import art
import os
from sounds import *
from inventory import *
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
        "marchand": self.marchand, 
        "boss": self.boss, 
        "piege": self.piege,
        "xp": self.xp
        }

        while player.is_alive():
            tprint("COMMANDE :")
            commandFound = False
            line = Entree("[italic]Entrez une commande[italic] (help pour afficher l'aide)", ">> ", True).run()
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
        print("[italic][#D2B4DE][bold]help[bold] pour voir cette page\n[bold]stats[bold] pour afficher les statistiques\n[bold]inventaire[bold] pour ouvrir l'inventaire\n[bold]heal[bold] pour utiliser vos potions\n[bold]explore[bold] pour avancer[#D2B4DE][italic]\n")
        print("Vous pouvez tomber sur les évenements suivants :\n")
        print("[red] -Combat (40%)\n[italic]    Lorsqu'un combat est lancé, vous pouvez essayer de fuire[red]\n[yellow]\n -Coffre (20%)\n    -Arme (augmente l'ATK)\n    -Armure (augmente la DEF)\n    -Potion (soigne les HP)[yellow][italic]\n\n [#ABEBC6]-Salle vide (10%)[#ABEBC6]\n\n[purple] -Piege (10%)[purple]\n\n[#D35400] -Marchand (10%)\n     Les marchands vendent tout ce qui se trouve dans les coffres du donjon[#D35400]\n\n[blue] -Couloir secret (10%)\n    -Boss\n    -Coffre\n    -Marchand[blue]")
        print("\n[#F9E79F]Attention ! Vous ne pouvez porter qu'une seule arme et qu'une seule armure à la fois !\n[italic]Prendez vous le risque de changer pour un équipement moins puissant ? :)[italic][#F9E79F]")
        Entree("\n[italic][green]Bonne chance ![green]\nAppuyez sur Entrée pour continuer ...[italic]", "", True).run()

    def explore(self, player, equip):
        avance = Event(player, equip)
        avance.explore(player, equip)
    
    def xp(self, player, equip):
        xp = Entree("[italic]Combien d'XP ?", "> ", True).run()
        a = Inventaire(player)
        a.ajouter_xp(player, int(xp))

    def fuite(self, player, equip):
        pass
        #Entree("Fuite", "> ", True).run()
    
    def combat(self, player, equip):
        Event.salle_monstre(self, player, equip)
    
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
        Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]", "", True).run()
    
    def coffre(self, player, equip):
        a = Event(player, equip)
        a.salle_coffre(player, equip)
        #Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]", "", True).run()

    def marchand(self, player, equip):
        a = Event(player, equip)
        a.salle_magasin(player, equip)
        #Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]", "", True).run()

    def heal(self, player, equip):
        #Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]", "", True).run()
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
                Entree(f"{potion.name} a été utilisé. Vous avez maintenant {player.health} / {player.max_health} HP.\n","", True).run()
            except (ValueError, IndexError):
                print("Vous ne vous soignez pas")
        else:
            Entree("Malheuserement, vous n'avez aucune potion !\n\n[italic]Appuez sur entrée pour continuer ... [italic]", "", True).run()
    
    def quit(self, player, equip):
        print(f"{player.name} quitte le jeu !")
        exit(0)

    def piege(self, player, equip):
        Event.salle_piege(self, player, equip)

    def boss(self, player, equip):
        Event.salle_monstre(self, player, equip, "boss")