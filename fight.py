from events import *
from caracter import Character
from sounds import *
from art import *
from random import choice
from screen import *
from inventory import *
import math

class Combat:
    def __init__(self, player, equip, enemy):
        self.player = player
        self.enemy = enemy
        self.equip = equip

    # def random_enemy(self):
    #     enemies = [CrawlingVermin(), ShadowStalker(), VenomousSerpent(), DeathbringerScorpion(), AbyssalHorror()]
    #     return choice(enemies)

    def battle(self, player, equip, enemy):
        if player.status == "combat":
            #goblin = Combat.random_enemy()
            os.system("cls")
            tprint("COMBAT")            
            print(f"C'est un {enemy.name} ! \n")
            tour = -1
            print(enemy.stats())
            Entree("", "> ").run()
            print(f"Vitesse de {player.name} = {player.vitesse}; vitesse de {enemy.name} = {enemy.vitesse}")
            if player.vitesse >= enemy.vitesse:
                print("Vous attaquerez en premier !")
            else:
                print("L'ennemi attaquera en premier !")
            os.system("cls")
            while player.is_alive() and enemy.is_alive():
                tprint(f"COMBAT vs {enemy.name} ")
                tprint(f"TOUR {tour+2} ")
                if player.vitesse >= enemy.vitesse:
                    player.attack(enemy)
                    time.sleep(2)
                    print("********\n")
                    enemy.attack(player)
                else:
                    enemy.attack(player)
                    time.sleep(2)
                    print("********\n")
                    player.attack(enemy)
                Entree("[italic]Appuyez sur Entrée pour passer au tour suivant ...[italic]", "", True).run()
                player.status = "normal"
                tour += 1      
            if player.is_alive():
                quit_pygame()
                time.sleep(0.1)
                sound_win_fight()
                tprint("COMBAT - VICTOIRE!")
                print(f"[green]Vous avez gagné ce combat ![green]")                
                Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]","", False).run()
                quantite_or = randint(1, 5)
                if player.type == "Thief":
                    print("[yellow](Bonus : Roublardise du voleur ! Or x2)[yellow]")
                    quantite_or *=2.5
                    quantite_or = math.ceil(quantite_or)
                equip.ajouter_or(player, quantite_or)
                Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]","", False).run()
                if tour == 0 :
                    player.OHKO +=1
                    time.sleep(0.1)
                    sound_OHKO()
                    print(f"[red]C'est un one-shot ![red]")
                    Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]","").run()
                else :
                    print(f"Combat terminé en {tour+2} tours !")
                    Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]","", False).run()               
                xp = randint(3,10)
                equip.ajouter_xp(player, xp)
                player.vitesse = player.vitesse_T
                player.kills +=1
                Entree("[italic]Appuyez sur Entrée pour continuer ...[italic]", "", True).run()
                if tour > player.tours_max:
                    player.tours_max = tour
                quit_pygame()    
                sound_bgm()
            enemy.regenerate()
        else:
            print("Mais t'es con t'es pas en combat")
