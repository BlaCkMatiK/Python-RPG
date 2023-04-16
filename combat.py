from evenement import *
from caracter import *
from sounds import *
from art import *

def battle(self):
    if self.status == "combat":
        time.sleep(1)
        goblin = random_enemy()
        os.system("cls")
        print(f"C'est un {goblin.name} ! \n")
        tour = -1
        print(f"Vitesse de {self.name} = {self.vitesse}; vitesse de {goblin.name} = {goblin.vitesse}")
        time.sleep(3)
        os.system("cls")
        while (self.is_alive() and goblin.is_alive()):
            if self.vitesse >= goblin.vitesse:
                print(f"Combat contre {goblin.name} / Tour {tour+2}\n----------------------\n")
                self.attack(goblin)
                time.sleep(2)
                print("********\n")
                goblin.attack(self)
                time.sleep(2)
                self.status = "normal"
                input("(Appuyez sur Entrée pour le tour suivant)")
                os.system("cls")
                tour +=1
            if self.vitesse < goblin.vitesse:
                print(f"Combat contre {goblin.name} / Tour {tour+2}\n----------------------\n")
                goblin.attack(self)
                time.sleep(2)
                print("********\n")
                self.attack(goblin)
                time.sleep(2)
                self.status = "normal"
                input("(Appuyez sur Entrée pour le tour suivant)")
                os.system("cls")
                tour +=1
        print(f"Combat terminé en {tour+1} tours !")        
        if self.is_alive():
            quit_pygame()
            time.sleep(0.1)
            sound_win_fight()
            tprint("VICTOIRE!")
            print(f"[green]Vous avez gagné ce combat ![green]")
            quantite_or = randint(0, 5)
            input(">>>")
            ajouter_or(self, quantite_or)
            self.vitesse = self.vitesse_T
            self.kills +=1
            input(">>>")
            quit_pygame()
            if tour == 0 :
                self.OHKO +=1
                time.sleep(0.1)
                sound_OHKO()
                print(f"[red]C'est un one-shot ![red]")
                input(">>>")
                os.system("cls")
            if tour > self.tours_max:
                self.tours_max = tour
            sound_bgm()
    else:
        print("Mais t'es con t'es pas en combat")
