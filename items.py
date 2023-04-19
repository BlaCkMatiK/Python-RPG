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


epee_bois = Epee("Epee en bois", 3, 2)
epee_fer = Epee("Epee en fer", 5, 4)
epee_or = Epee("Epee en or", 7, 5)
epee_diamant = Epee("Epee en diamant", 20, 8)
epee_destructeur= Epee("Epee destructrice", 50, 30)

sceptre_debutant = Sceptre("Sceptre débutant", 3, 2 )
sceptre_apprenti = Sceptre("Sceptre d'apprenti", 5, 3)
sceptre_intermediaire = Sceptre("Sceptre intermediaire", 7, 4)
sceptre_avance = Sceptre("Sceptre avance", 12, 6)
sceptre_mage = Sceptre("Sceptre de mage", 20, 8)
sceptre_destructeur = Sceptre("Sceptre destructeur", 50, 30)

armes_list = [epee_bois, epee_fer, epee_or, epee_diamant, epee_destructeur, sceptre_debutant, sceptre_apprenti, sceptre_intermediaire, sceptre_avance, sceptre_mage, sceptre_destructeur]

def random_arme():
    return choice(armes_list)

class Armure(Item):
    type="armure"
    def __init__(self, name, price, bonus, bonus_class=None):
        super().__init__(name, price, bonus, associated_player=None)
        self.bonus_class = bonus_class
    def __str__(self):
        return f"[#85C1E9]{self.name} (+{self.bonus} DEF)[#85C1E9]"


armure_cuir = Armure("Armure en cuir", 10, 2)
armure_cuivre = Armure("Armure en cuivre", 15, 5)
armure_fer = Armure("Cottes de maille", 18, 7)
armure_diamant = Armure("Armure en diamant ", 25, 15)
armure_ultime = Armure("Armure en diamant ", 50, 30)

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
    
potion_2hp = Potion("Potion médiocre 2HP", 5, 2)
potion_4hp = Potion("Petite potion 4HP", 10, 4)
potion_8hp = Potion("Potion moyenne 8HP", 15, 8)
potion_10hp = Potion("Potion respectable 15HP", 25, 15)
potion_20hp = Potion("Potion haut de gamme 20HP", 45, 20)
potion_100hp = Potion("Potion ultime 100HP", 75, 100)

potions_list = [potion_2hp, potion_4hp, potion_8hp, potion_10hp, potion_20hp ,potion_100hp]

def random_potion():
    return choice(potions_list)