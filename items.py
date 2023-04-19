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
epee_fer = Epee("Epee en fer", 10, 4)

sceptre_guez = Sceptre("Sceptre nul",10, 2 )

armes_list = [epee_bois, epee_fer, sceptre_guez]

def random_arme():
    return choice(armes_list)

class Armure(Item):
    type="armure"
    def __init__(self, name, price, bonus, bonus_class=None):
        super().__init__(name, price, bonus, associated_player=None)
        self.bonus_class = bonus_class
    def __str__(self):
        return f"[#85C1E9]{self.name} (+{self.bonus} DEF)[#85C1E9]"

quoicou_armure = Armure("Armure en quoicoubeh", 10, 1)
armure_cuir = Armure("Armure en cuir", 10, 2)
armure_cuivre = Armure("Armure en cuivre", 10, 5)
armure_fer = Armure("Cottes de maille", 10, 7)

armures_list = [armure_cuir, armure_fer, quoicou_armure, armure_cuivre]

def random_armure():
    return choice(armures_list)

class Potion(Item):
    type="potion"
    def __init__(self, name, price, bonus):
        super().__init__(name, price, bonus, associated_player=None)
        self.bonus = bonus

    def __str__(self):
        return f"[#BB8FCE]{self.name} (+{self.bonus} HP [#BB8FCE])"
    
potion_2hp = Potion("Potion 2HP", 5, 2)
potion_4hp = Potion("Potion 4HP", 10, 4)
potion_10hp = Potion("Potion 10HP", 15, 10)

potions_list = [potion_2hp, potion_4hp, potion_10hp]

def random_potion():
    return choice(potions_list)

print(epee_fer.type)