from caracter import *

class Item(object):
    def __init__(self, name, price, bonus, associated_player=None):
        self.name = name
        self.price = price
        self.bonus = bonus
        self.associated_player = associated_player

class Arme(Item):
    def __init__(self, name, price, bonus, bonus_class=None, associated_player=None):
        super().__init__(name, price, bonus, associated_player)
        self.bonus_class = bonus_class

    def __str__(self):
        return f"{self.name} (+{self.bonus} ATK)"

epee_bois = Arme("Epee en bois", 3, 2)
epee_fer = Arme("Epee en fer", 10, 4)

armes = [epee_bois, epee_fer]

def random_arme():
    return choice(armes)

class Armure(Item):
    def __init__(self, name, price, bonus, bonus_class=None):
        super().__init__(name, price, bonus, associated_player=None)
        self.bonus_class = bonus_class
    def __str__(self):
        return f"{self.name} (+{self.bonus} DEF)"

armure_cuir = Armure("Armure en cuir", 10, 2)
armure_fer = Armure("Cottes de maille", 10, 5)

armures = [armure_cuir, armure_fer]

def random_armure():
    return choice(armures)

class Potion(Item):
    def __init__(self, name, price, bonus):
        super().__init__(name, price, bonus, associated_player=None)
        self.bonus = bonus

    def __str__(self):
        return f"{self.name} (+{self.bonus} HP)"
potion_2hp = Potion("Potion 2HP", 5, 2)
potion_4hp = Potion("Potion 4HP", 10, 4)
potion_10hp = Potion("Potion 10HP", 15, 10)

potions = [potion_2hp, potion_4hp, potion_10hp]

def random_potion():
    return choice(potions)