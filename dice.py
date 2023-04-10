import random

        
class Dice:
    type = "dice"
    
    def __init__(self, faces=6):
        self.faces = faces
    
    def roll(self):
        return random.randint(1, self.faces)
    
    def __str__(self):
        return f"I'm a {self.faces} faces {type(self).type}"
    

        
class RiggedDice(Dice):
    type = "rigged dice"
    
    def roll(self, rigged=False):
        super().roll() if not rigged else self.faces

class WoodDice(Dice):
    type = "wood dice"


if __name__ == "__main__":
    
    print("\n")
    
    my_dice = Dice(10)
    my_dice2 = Dice(100)
    print(type(my_dice))
    print(my_dice)
    print(my_dice.roll())
    
    my_rigged_dice = RiggedDice(20)
    print(my_rigged_dice)
    print(my_rigged_dice.roll(True))

    a_wood_dice = WoodDice(12)
    print(a_wood_dice)

    for i in range(0, 1000):
        print(f"Launch {i + 1}: {my_dice.roll()}")