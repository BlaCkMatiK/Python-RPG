import random

from caracter import *
from screen import *
from inventaire import *
from combat import Combat
from items import *

class Event:
    def __init__(self, player, equip):
        self.player = player
        self.equip = equip

    def explore(self, player, equip):
        events_list = [
            ("vide"),
            ("coffre"),
            ("monstre"),
            ("magasin"),
            ("piege"),
            ("couloir"),
        ]
        events_prob = [0.1, 0.2, 0.4, 0.1, 0.1, 0.1]

        event = self._weighted_choice(events_list, events_prob)

        if event == "vide":
            self.salle_vide(player, equip)
        elif event == "coffre":
            self.salle_coffre(player, equip)
        elif event == "monstre":
            self.salle_monstre(player, equip)
        elif event == "magasin":
            self.salle_magasin(player, equip)
        elif event == "piege":
            self.salle_piege(player, equip)
        elif event == "couloir":
            self.salle_couloir(player, equip)

    def salle_vide(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print(f"{player.name} trouve salle vide")
        input()
        os.system("cls")

    def salle_coffre(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print("Vous avez trouvé un coffre !")
        if input("Voulez-vous l'ouvrir ? (Oui/Non) - ").lower().startswith("o"):
            print("Le coffre s'ouvre ...")
            sound_chest_o()
            time.sleep(2)
            """ Fonction qui retourne un item aléatoire parmi une arme, une armure ou de l'or """
            item_1 = random_arme()
            item_2 = random_armure()
            item_3 = random_potion()
            items = [item_1, item_2, item_3]
            item_choisi = choice(items)
            if item_choisi == item_1:
                equip.ajouter_arme(player, item_choisi)
            elif item_choisi == item_2:
                equip.ajouter_armure(player, item_choisi)
            elif item_choisi == item_3:
                equip.ajouter_potion(player, item_choisi)
            else:
                quantite_or = random.randint(1, 10)
                equip.ajouter_or(player, quantite_or)
            sound_item()
            time.sleep(2)
            print("Vous fermez le coffre")
            sound_chest_c()
            player.chests +=1
            wait_input()
        else:
            print("Vous n'avez pas ouvert ce coffre.")
            wait_input()
    
    def salle_monstre(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        time.sleep(0.1)
        quit_pygame()
        sound_battle()
        print("%s rencontre %s" % (player.name, 'un ennemi !'))
        if input("Veux tu te battre ou tenter de fuire? (Combat / Fuite)\n>").lower().startswith("c"):
            player.status = "combat"
            enemy = random_enemy()
            battle = Combat(player, equip, enemy)
            battle.battle(player, equip, enemy)
        else :
            print("vous fuyez !")

    def salle_magasin(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print("Il y a un marchand !")
        choix=input("Rentrer dans le magasin ? (Oui/Non) - ")
        if choix.lower().startswith("o"):
            quit_pygame()
            print("Vous entrez dans le magasin")
            sound_marchand()
            time.sleep(2)
            os.system("cls")
            tprint("MARCHAND")
            sound_shop()
            # variable var_1 qui est un nombre random entre 1 et 3
            var_1 = randint(1, 3)
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
                print("1 - Epee en bois (10 or)\n2 - Epee en fer (20 or)\n3 - Epee en or (30 or)\n4 - Epee en diams (40 or)\n")
                choix=input("Que voulez vous acheter  ? - ")
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
                choix=input("Que voulez vous acheter  ? - ")
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
                choix=input("Que voulez vous acheter  ? - ")

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
            var_2 = randint(1, 1000)
            if var_2 >= 1 and var_2 <= 300:

                print("Aurevoir cher ami !")
            elif var_2 >= 301 and var_2 <= 600:
                print("Bonne journée en esperant vous revoir au plus vite")
            elif var_2 >= 601 and var_2 <= 999:
                print("Le marchant vous souhaite une bonne journée !")
            elif var_2 == 1:
                print("Oh le rat")
        wait_input()
        os.system("cls")

    def salle_piege(self, player, equip):
        os.system("cls")
        tprint("SALLE")
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
        player.health -= 2
        player.traps +=1
        os.system("cls")
    
    def salle_couloir(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print(f"{player.name} trouve salle couloir")
        input()
        os.system("cls")

    def _weighted_choice(self, list, prob):
        """Choix pondéré d'un évenement

        Args:
            list (list): nom evenements
            prob (list): probabilités
        """
        # Select a random choice based on a probability distribution
        return choices(list, prob)[0]

# from caracter import *
# import random
# from rich import print
# from screen import over, wait_input
# import time
# from sounds import *
# from art import *
# from combat import Combat
# from inventaire import *

# a_dice=Dice(6)



# def explore(self):
#     if self.status != "combat":
#         self.steps += 1
#         print("%s explore un passage étroit." % self.name)
#         time.sleep(1)
#         res = randint(1, 10)
#         print(f"Dé : {res}")
#         if res <= 1:
#             marchand(self)
#         elif res > 1 and res <= 5:
#             rencontre(self)
#         elif res > 5 and res < 8:
#             ouvrir_coffre(self)
#         elif res > 8:
#             piege(self)
#         elif res == 9:
#             couloir(self)
#         else:
#             print("Ouf ! Il ne se passe rien dans cette salle")
#             wait_input()
#     else:
#         print("Vous ne pouvez pas partir comme ça")
 

# def fuite(self):
#     if self.status == "combat":
#         res = randint(0, self.discrétion)
#         print(f"dé :{res}")
#         if res > 4:
#             self.status = "normal"
#             print("Vous avez réussi à fuire")
#             quit_pygame()
#             sound_bgm()
#         else:
#             print("Vous n'avez pas réussi a fuire")
#             self.status = "combat"
#             self.vitesse_T = self.vitesse
#             self.vitesse = 0
#             Commands["combat"](self)
#     else:
#         print("Mais vous n'êtes pas en combat")

# def rencontre(self):
#     