from caracter import *
import random
from rich import print
from combat import battle
from screen import over, wait_input
import time
from sounds import *
from art import *
from combat import *
from inventaire import *


a_dice=Dice(6)

def help(self):
    os.system("cls")
    tprint("PAGE D'AIDE")
    print("\n[italic][bold]explore[bold] pour avancer\n[bold]hp[bold] pour connaitre ses points de vie\n[bold]help[bold] pour voir cette page\n[italic]")
    wait_input()

def explore(self):
    if self.status != "combat":
        self.steps += 1
        print("%s explore un passage étroit." % self.name)
        time.sleep(1)
        res = randint(1, 10)
        print(f"dé :{res}")
        if res == 1:
            print("Il y a un marchand !")
            wait_input()
        elif res > 1 and res <= 5:
            rencontre(self)
        elif res > 5 and res < 8:
            ouvrir_coffre(self)
        elif res > 8:
            piege(self)
        else:
            print("Ouf ! Il ne se passe rien dans cette salle")
            wait_input()
    else:
        print("Vous ne pouvez pas partir comme ça")

def piege(self):
    print("Tout est très calme dans cette pièce...")
    for i in range(0, 3):
        time.sleep(1)
        print(".")
    time.sleep(1)
    print("OHHH NON vous venez de vous prendre un piège!")
    sound_trap()
    time.sleep(1)
    print("Vous avez perdu 2hp :/ ")
    wait_input()
    self.health = self.health - 2
    self.traps +=1

def fuite(self):
    if self.status == "combat":
        res = randint(0, self.discrétion)
        print(f"dé :{res}")
        if res > 4:
            self.status = "normal"
            print("Vous avez réussi à fuire")
        else:
            print("Vous n'avez pas réussi a fuire")
            self.status = "combat"
            self.vitesse_T = self.vitesse
            self.vitesse = 0
            Commands["combat"](self)
    else:
        print("Mais vous n'êtes pas en combat")

def rencontre(self):
    time.sleep(0.1)
    quit_pygame()
    sound_battle()
    print("%s rencontre %s" % (self.name, 'un ennemi !'))
    print("Veux tu te battre ou tenter de fuire? ('combat' ou 'fuite')")
    self.status = "combat"
    line = input(">> ")
    args = line.split()
    if len(args) > 0:
        commandFound = False
        for c in Commands.keys():
            if args[0] == c[:len(args[0])]:
                Commands[c](self)
                commandFound = True
                break
        if not commandFound:
            print("%s ne comprend pas." % self.name)

def ouvrir_coffre(self):
        print("Vous avez trouvé un coffre !")
        choix=input("Voulez-vous l'ouvrir ? (Oui/Non)")
        if choix.lower().startswith("o"):
            print("Le coffre s'ouvre ...")
            sound_chest_o()
            time.sleep(2)
            """ Fonction qui retourne un item aléatoire parmi une arme, une armure ou de l'or """
            items = ["arme", "armure", "or", "potion"]
            item_choisi = random.choice(items)
            if item_choisi == "arme":
                print("Vous avez trouvé une arme !")
                ajouter_arme(self, item_choisi)
            elif item_choisi == "armure":
                print("Vous avez trouvé une armure !")
                ajouter_armure(self, item_choisi)
            elif item_choisi == "potion":
                print("Vous avez trouvé une potion !")
                ajouter_potion(self, item_choisi)
            else:
                quantite_or = random.randint(1, 10)
                ajouter_or(self, quantite_or)
            sound_item()
            time.sleep(2)
            print("Vous fermez le coffre")
            sound_chest_c()
            self.chests +=1
            wait_input()
        else:
            print("Vous n'avez pas ouvert ce coffre.")
            wait_input()

def loose_hp(player):
    print(f"{player.health} - 10 = {player.health - 100}")
    player.health -= 100

def konami(self):
    print("Haut, Haut, Bas, Bas, Gauche, Droite, Gauche, Droite, B, A")

def choose_event(player):
    while (Character.is_alive(player)):
        tprint("CHOIX DE L'ACTION")
        print("[italic][bold]help[bold] pour afficher l'aide[italic]\n")
        line = input(">> ")
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](player)
                    commandFound = True
                    break
            if not commandFound:
                os.system("cls")
                print("%s ne comprend pas." % player.name)
    print(f"{player.name} n'a plus de vie !")
    time.sleep(2)
    quit_pygame()
    
def over_e(player):
    over()

Commands = {
    'stats': stats,
    # 'quit': Player.quit,
    'help': help,
    # 'status': Player.status,
    # 'rest': Player.rest,
    'over': over_e,
    'explore': explore,
    'fuite': fuite,
    'combat': battle,
    'hp': Character.show_health,
    'xp': Character.show_xp,
    '+xp': ajouter_xp,
    'inventaire': afficher_inventaire,
    'loose': loose_hp,
    'konami': konami,
    'fight': battle
}

if __name__ == "__main__":
    self = create_character()
    ouvrir_coffre(self)
