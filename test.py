import random

class Fighter:
    def __init__(self, name, hp, atk, spd):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.spd = spd
        self.defending = False
    
    def attack(self):
        return random.randint(1, self.atk)
    
    def defend(self):
        self.defending = True
    
    def take_damage(self, damage):
        if self.defending:
            damage //= 2
            self.defending = False
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def is_alive(self):
        return self.hp > 0
    
    def get_name(self):
        return self.name
    
    def get_speed(self):
        return self.spd
    
class Battle:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        
    def start(self):
        print(f"{self.fighter1.get_name()} vs {self.fighter2.get_name()}!")
        while self.fighter1.is_alive() and self.fighter2.is_alive():
            if self.fighter1.get_speed() > self.fighter2.get_speed():
                self.fighter2.take_damage(self.fighter1.attack())
                if not self.fighter2.is_alive():
                    break
                self.fighter1.defending = False
                action = input("Enter 'a' to attack, or 'd' to defend: ")
                if action == 'a':
                    self.fighter1.take_damage(self.fighter2.attack())
                elif action == 'd':
                    self.fighter1.defend()
            else:
                self.fighter1.take_damage(self.fighter2.attack())
                if not self.fighter1.is_alive():
                    break
                self.fighter2.defending = False
                action = input("Enter 'a' to attack, or 'd' to defend: ")
                if action == 'a':
                    self.fighter2.take_damage(self.fighter1.attack())
                elif action == 'd':
                    self.fighter2.defend()
        
        if self.fighter1.is_alive():
            print(f"{self.fighter1.get_name()} wins!")
        else:
            print(f"{self.fighter2.get_name()} wins!")
        
# Create the characters
character = Fighter("Hero", 100, 20, 10)
goblin = Fighter("Goblin", 50, 10, 5)

# Start the battle
battle = Battle(character, goblin)
battle.start()
