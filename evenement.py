from random import *
from caracter import *
import random
from rich import print
from screen import over


a_dice=Dice(6)


def explore(self):
    if self.status != "combat":
        print("%s explore un passage étroit." % self.name)
        res = randint(1, 10)
        if res <= 5:
            print("%s rencontre %s" % (self.name, 'un ennemi !'))
            print("Veux tu te battre ou tenter de fuire? ('combat' ou 'fuite')")
            self.status = "combat"
        elif res > 5 and res < 8:
            print("Vous avez trouvé un coffre !")
            ouvrir_coffre(self)
        elif res > 8:
            print("Tout est très calme dans cette pièce...")
            for i in range(0, 3):
                time.sleep(1)
                print(".")
            time.sleep(1)
            print("OHHH NON vous venez de vous prendre un piège!")
            time.sleep(1)
            print("Vous avez perdu 2hp :/ ")
            self.health = self.health - 2
    else:
        print("Vous ne pouvez pas partir comme ça")

def fuite(self):
    if self.status == "combat":
        res = randint(0, self.discrétion)
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

def random_enemy():
    enemies = [CrawlingVermin(), ShadowStalker(), VenomousSerpent(), DeathbringerScorpion(), AbyssalHorror()]
    return random.choice(enemies)

def combat(self):
    if self.status == "combat":
        time.sleep(1)
        goblin = random_enemy()
        print(f"C'est un {goblin.name} ! \n")
        while (self.is_alive() and goblin.is_alive()):
            if self.vitesse >= goblin.vitesse:
                self.attack(goblin)
                time.sleep(1)
                goblin.attack(self)
                time.sleep(1)
                self.status = "normal"
            if self.vitesse < goblin.vitesse:
                goblin.attack(self)
                time.sleep(1)
                self.attack(goblin)
                time.sleep(1)
                self.status = "normal"
        if self.is_alive():
            quantite_or = randint(0, 5)
            ajouter_or(self, quantite_or)
            self.vitesse = self.vitesse_T
    else:
        print("Mais t'es con t'es pas en combat")

def ajouter_or(self, quantite_or):
        """ Ajoute de l'or à l'inventaire du personnage """
        self.gold += quantite_or
        print(
            f"[yellow]{self.name} a trouvé {quantite_or} pièces d'or ![yellow]")

def ouvrir_coffre(self):
        print("Le coffre s'ouvre")
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

def ajouter_arme(self, arme):
        """ Ajoute une arme à l'inventaire du personnage """
        self.armes.append(arme)
        print(f"{self.name} a ajouté {arme} à son inventaire.")

def ajouter_armure(self, armure):
    """ Ajoute une armure à l'inventaire du personnage """
    self.armures.append(armure)
    print(f"{self.name} a ajouté {armure} à son inventaire.")

def ajouter_potion(self, potion):
    """ Ajoute une potion à l'inventaire du personnage """
    self.potions.append(potion)
    print(f"[purple]{self.name} a trouvé une {potion} ![/purple]")

def afficher_inventaire(self):
    """ Affiche l'inventaire complet du personnage """
    print(f"Inventaire de {self.name}:")
    print(f"- Or: {self.gold}")
    print("- Armes: ")
    for arme in self.armes:
        print(f"  - {arme}")
    print("- Armures: ")
    for armure in self.armures:
        print(f"  - {armure}")

def loose_hp(player):
    print(f"{player.health} - 10 = {player.health}")
    player.health -= 10

def choose_event(player):
    while (Character.is_alive(player)):
        line = input("> ")
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](player)
                    commandFound = True
                    break
            if not commandFound:
                print("%s ne comprend pas." % player.name)
    print("Tu es mort ^^")

def over_e(player):
    over()

Commands = {
    # 'quit': Player.quit,
    # 'help': Player.help,
    # 'status': Player.status,
    # 'rest': Player.rest,
    'over': over_e,
    'explore': explore,
    'fuite': fuite,
    'combat': combat,
    'hp': Character.show_health,
    'inventaire': afficher_inventaire,
    'loose': loose_hp
}


# for i in range (100):
#     print (randint(0,4))
