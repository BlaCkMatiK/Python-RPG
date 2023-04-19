from evenement import *
from caracter import Character
from sounds import *
from art import *
from random import choice
from screen import *
from inventaire import *

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
            print(f"Vitesse de {player.name} = {player.vitesse}; vitesse de {enemy.name} = {enemy.vitesse}")
            if player.vitesse >= enemy.vitesse:
                print("Vous attaquerez en premier !")
            else:
                print("L'ennemi attaquera en premier !")
            enemy.stats()
            os.system("cls")
            while player.is_alive() and enemy.is_alive():
                tprint(f"COMBAT vs {enemy.name} ")
                tprint(f"TOUR {tour+2} ")
                if player.vitesse >= enemy.vitesse:
                    player.attack(enemy)
                    time.sleep(2)
                    print("********\n")
                    enemy.attack(player)
                    wait_input_turn()
                else:
                    enemy.attack(player)
                    time.sleep(2)
                    print("********\n")
                    player.attack(enemy)
                    wait_input_turn()
                player.status = "normal"
                os.system("cls")
                tour += 1      
            if player.is_alive():
                quit_pygame()
                time.sleep(0.1)
                sound_win_fight()
                tprint("COMBAT - VICTOIRE!")
                print(f"[green]Vous avez gagné ce combat ![green]")
                quantite_or = randint(0, 5)
                wait_input_pass()
                equip.ajouter_or(player, quantite_or)
                xp = randint(3,10)
                wait_input_pass()
                equip.ajouter_xp(player, xp)
                player.vitesse = player.vitesse_T
                player.kills +=1
                wait_input_pass()
                if tour == 0 :
                    player.OHKO +=1
                    time.sleep(0.1)
                    sound_OHKO()
                    print(f"[red]C'est un one-shot ![red]")
                    wait_input()
                else :
                    print(f"Combat terminé en {tour+2} tours !")
                    wait_input()

                if tour > player.tours_max:
                    player.tours_max = tour
                quit_pygame()    
                sound_bgm()
            enemy.regenerate()
        else:
            print("Mais t'es con t'es pas en combat")
