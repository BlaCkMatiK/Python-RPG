from evenement import *
from caracter import Character
from sounds import *
from art import *
from inventaire import *
from random import choice
from screen import *

class Combat:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def random_enemy(self):
        enemies = [CrawlingVermin(), ShadowStalker(), VenomousSerpent(), DeathbringerScorpion(), AbyssalHorror()]
        return choice(enemies)

    def battle(self):
        if self.status == "combat":
            goblin = Combat.random_enemy()
            os.system("cls")
            tprint("COMBAT")
            print(f"C'est un {goblin.name} ! \n")
            tour = -1
            print(f"Vitesse de {self.name} = {self.vitesse}; vitesse de {goblin.name} = {goblin.vitesse}")
            time.sleep(2)
            os.system("cls")
            while self.is_alive() and goblin.is_alive():
                tprint(f"COMBAT vs {goblin.name} ")
                tprint(f"TOUR {tour+2} ")
                if self.vitesse >= goblin.vitesse:
                    self.attack(goblin)
                    time.sleep(2)
                    print("********\n")
                    goblin.attack(self)
                    wait_input_turn()
                else:
                    goblin.attack(self)
                    time.sleep(2)
                    print("********\n")
                    self.attack(goblin)
                    wait_input_turn()
                self.status = "normal"
                os.system("cls")
                tour += 1      
            if self.is_alive():
                quit_pygame()
                time.sleep(0.1)
                sound_win_fight()
                tprint("COMBAT - VICTOIRE!")
                print(f"[green]Vous avez gagné ce combat ![green]")
                quantite_or = randint(0, 5)
                wait_input_pass()
                ajouter_or(self, quantite_or)
                xp = randint(3,10)
                wait_input_pass()
                ajouter_xp(self, xp)
                self.vitesse = self.vitesse_T
                self.kills +=1
                wait_input_pass()
                if tour == 0 :
                    self.OHKO +=1
                    time.sleep(0.1)
                    sound_OHKO()
                    print(f"[red]C'est un one-shot ![red]")
                    wait_input()
                else :
                    print(f"Combat terminé en {tour+1} tours !")
                    wait_input()

                if tour > self.tours_max:
                    self.tours_max = tour
                quit_pygame()    
                sound_bgm()
        else:
            print("Mais t'es con t'es pas en combat")
