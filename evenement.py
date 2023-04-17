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
    print("[italic]explore pour avancer[italic]\nVous pouvez tomber sur les évenements suivants :\n -Combat (40%)\n -Coffre (20%)\n -Salle vide (10%)\n -Piege (10%)\n -Marchand (10%)\n -Couloir secret (10%) ")
    print("\n""[#C39BD3]hp[#C39BD3]"" pour connaitre ses points de vie\n""[#C39BD3]help[#C39BD3]"" pour voir cette page\n""[#C39BD3]inventaire[#C39BD3]"" pour ouvrir l'inventaire[italic]")
    print("")
    print("[italic]lorsque un combat est lancé, vous pouvez essayer de fuire avec [#C39BD3]fuite[#C39BD3]")
    wait_input()

def explore(self):
    if self.status != "combat":
        self.steps += 1
        print("%s explore un passage étroit." % self.name)
        time.sleep(1)
        res = randint(1, 10)
        print(f"Dé : {res}")
        if res <= 1:
            marchand(self)
        elif res > 1 and res <= 5:
            rencontre(self)
        elif res > 5 and res < 8:
            ouvrir_coffre(self)
        elif res > 8:
            piege(self)
        elif res == 9:
            couloir(self)
        else:
            print("Ouf ! Il ne se passe rien dans cette salle")
            wait_input()
    else:
        print("Vous ne pouvez pas partir comme ça")

def couloir(self):
    print("Il y a un couloir !")
    wait_input()

def marchand(self):
    print("Il y a un marchand !")
    choix=input("Rentrer dans le magasin ? (Oui/Non)")
    if choix.lower().startswith("o"):
        quit_pygame()
        print("Vous entrez dans le magasin")
        sound_marchand()
        time.sleep(2)
        os.system("cls")
        tprint("MARCHAND")        
        sound_shop()
        # variable var_1 qui est un nombre random entre 1 et 3
        var_1 = random.randint(1, 3)
        if var_1 == 1:
            print("Bonjour marchand certifié sudosu pour vous servir, Que voulez-vous aujourd'hui ?")
        elif var_1 == 2:
            print("Bonjour aventurier quel bien vous ferez plaisir aujourd'hui ?")
        else:
                print("C'est quelle heure pour acheter du materiel chef ?")

        print("\n1 - Arme ⚔️ \n2 - Armure 🛡️ \n3 - Soin ❤️\n")
        choix=input("Qu'est-ce qui vous intéresse ?")

        #Arme
        if choix.lower().startswith("1"):
            os.system("cls")
            tprint("MARCHAND - ARMES")
            print("1 - Epee en bois       10 or\n2 - Epee en fer       20 or\n3 - Epee en or       30 or\n4 - Epee en diams       40 or\n")
            choix=input("Que voulez vous acheter  ?")
            if choix.lower().startswith("1"):
                print("Vous avez acheté une epee en bois")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
            if choix.lower().startswith("2"):
                print("Vous avez acheté une epee en fer")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
            if choix.lower().startswith("3"):
                print("Vous avez acheté une epee en or")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
            if choix.lower().startswith("4"):
                print("Vous avez acheté une epee en diams")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
        
        #Armure
        elif choix.lower().startswith("2"):
            os.system("cls")
            tprint("MARCHAND - ARMURES")
            print("1 - Armure en bois       10 or")
            print("2 - Armure en fer       20 or")
            print("3 - Armure en or       30 or")
            print("4 - Armure en diams       40 or")
            choix=input("Que voulez vous acheter  ?")
            if choix.lower().startswith("1"):
                print("Vous avez acheté une Armure en bois")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
            elif choix.lower().startswith("2"):
                print("Vous avez acheté une Armure en fer")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
            elif choix.lower().startswith("3"):
                print("Vous avez acheté une Armure en or")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
            elif choix.lower().startswith("4"):
                print("Vous avez acheté une Armure en diams")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
        
        #Soins
        else:
            os.system("cls")
            tprint("MARCHAND - SOINS")
            print("1 - Potion de soin       10 or")
            choix=input("Que voulez vous acheter  ?")
                
            if choix.lower().startswith("1"):
                print("Vous avez acheté une Potion de soin")
                #Verif que le player a assez de thune 
                # retirer la thune 
                # donner l'item
        quit_pygame()
        sound_item()
        time.sleep(4)
        sound_bgm()
    else:
        var_2 = random.randint(1, 1000)
        if var_2 >= 1 and var_2 <= 300:

            print("Aurevoir cher ami !")
        elif var_2 >= 301 and var_2 <= 600:
            print("Bonne journée en esperant vous revoir au plus vite")
        elif var_2 >= 601 and var_2 <= 999:
            print("Le marchant vous souhaite une bonne journée !")
        elif var_2 == 1:
            print("Oh le rat")
        wait_input()
    wait_input()

def piege(self):
    print("Tout est très calme dans cette pièce...")
    for i in range(0, 3):
        time.sleep(1)
        print(".")
    time.sleep(1)
    print("\nAie ! Vous venez de vous prendre un piège!")
    sound_trap()
    time.sleep(1)
    print("Vous avez perdu 2 HP ❤️ ")
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
            quit_pygame()
            sound_bgm()
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

Commands = {
    'stats': stats,
    'help': help,
    'explore': explore,
    'fuite': fuite,
    'combat': battle,
    'inventaire': afficher_inventaire,
    'loose': loose_hp,
    'konami': konami,
}