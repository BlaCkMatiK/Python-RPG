from caracter import *
from rich import *

class Item(object):
    def __init__(self, name, price, bonus, associated_player=None):
        self.name = name
        self.price = price
        self.bonus = bonus
        self.associated_player = associated_player

class Arme(Item):
    type="arme"
    def __init__(self, name, price, bonus, associated_player=None):
        super().__init__(name, price, bonus, associated_player)

    def __str__(self):
        return f"[#F1948A]{self.name} (+{self.bonus} ATK)[#F1948A]"

class Epee(Arme):
    def __init__(self, name, price, bonus, classe = "Warrior"):
        super().__init__(name, price, bonus, associated_player=None)
        self.classe = classe

class Sceptre(Arme):
    def __init__(self, name, price, bonus, classe = "Mage"):
        super().__init__(name, price, bonus, associated_player=None)
        self.classe = classe

class Dague(Arme):
    def __init__(self, name, price, bonus, classe = "Voleur"):
        super().__init__(name, price, bonus, associated_player=None)
        self.classe = classe

epee_bois = Epee("Epee classique", 5, 1)
epee_fer = Epee("Epee lourde", 10, 3)
epee_or = Epee("Epee tranchante", 15, 5)
epee_diamant = Epee("Epee du roi", 20, 8)
epee_destructeur= Epee("Epee ultime", 35, 15)

sceptre_debutant = Sceptre("Sceptre classique", 5, 1 )
sceptre_apprenti = Sceptre("Sceptre ancien", 10, 3)
sceptre_intermediaire = Sceptre("Sceptre antique", 15, 5)
sceptre_mage = Sceptre("Sceptre mythique", 20, 8)
sceptre_destructeur = Sceptre("Sceptre ultime", 35, 15)

dague_fer = Dague("Dague classique", 5, 1)
dague_or = Dague("Dague lourde", 10, 3)
dague_diamant = Dague("Dague tranchante", 15, 5)
dague_longue = Dague("Dague du roi", 20, 8)
dague_destructeur= Dague("Dague ultime", 35, 15)

armes_list = [epee_bois, epee_fer, epee_or, epee_diamant, epee_destructeur, sceptre_debutant, sceptre_apprenti, sceptre_intermediaire, sceptre_mage, sceptre_destructeur, dague_fer, dague_or, dague_diamant, dague_longue, dague_destructeur]

def random_arme():
    return choice(armes_list)

class Armure(Item):
    type="armure"
    def __init__(self, name, price, bonus, bonus_class=None):
        super().__init__(name, price, bonus, associated_player=None)
        self.bonus_class = bonus_class
    def __str__(self):
        return f"[#85C1E9]{self.name} (+{self.bonus} DEF)[#85C1E9]"


armure_cuir = Armure("Armure en cuir", 4, 2)
armure_cuivre = Armure("Armure en cuivre", 10, 5)
armure_fer = Armure("Cottes de maille", 20, 15)
armure_diamant = Armure("Armure en diamant ", 30, 25)
armure_ultime = Armure("Armure ultime ", 40, 35)
armures_list = [armure_cuir, armure_fer, armure_cuivre, armure_fer, armure_diamant, armure_ultime]

def random_armure():
    return choice(armures_list)

class Potion(Item):
    type="potion"
    def __init__(self, name, price, bonus):
        super().__init__(name, price, bonus, associated_player=None)
        self.bonus = bonus

    def __str__(self):
        return f"[#BB8FCE]{self.name} (+{self.bonus} HP [#BB8FCE])"
    
potion_2hp = Potion("Potion médiocre", 5, 2)
potion_4hp = Potion("Petite potion", 10, 4)
potion_8hp = Potion("Potion moyenne", 15, 8)
potion_10hp = Potion("Potion respectable", 25, 15)
potion_20hp = Potion("Potion haut de gamme", 45, 20)
potion_100hp = Potion("Potion ultime", 75, 100)

potions_list = [potion_2hp, potion_4hp, potion_8hp, potion_10hp, potion_20hp ,potion_100hp]

def random_potion():
    return choice(potions_list)