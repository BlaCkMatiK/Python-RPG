#import rich
import os
import random

from caracter import *
from dice import Dice
from evenement import *
from screen import *


def main():
    title()
    os.system("cls")
    player = create_character()
    #stats(player)
    while Character.is_alive(player):
        choose_event(player)
    over()

if __name__ == "__main__":
    main()
    