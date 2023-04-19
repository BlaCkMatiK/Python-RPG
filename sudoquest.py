#import rich
import os
import random
import time

from caracter import create_character
from dice import Dice
from evenement import *
from screen import *
import signal
import threading
from sounds import *

from commandes import Commandes
from inventaire import Inventaire

def handle_signal(signal_num, frame):
    os.system("cls")
    print("Fermeture du jeu prématurée par l'utilisateur (Ctrl+C) \n2 sec. avant fermeture")
    time.sleep(1)
    os.system("cls")
    exit(0)

signal.signal(signal.SIGINT, handle_signal)

def start():
    startup()    
    sound_create()
    if input("Passer histoire ? (Oui / Non) - ").lower().startswith("o"):
        pass
    else :
        story()

def main():
    player_b = create_character()
    stuff = Inventaire(player_b)
    quit_pygame()
    sound_enter()
    time.sleep(10)
    os.system("cls")
    sound_bgm()
    #stats(player)
    while player_b.is_alive():
        action = Commandes(player_b, stuff)
        action.choix(player_b, stuff)
    #over()
    print_game_over()
    end_stats(player_b)
    main()

if __name__ == "__main__":
    start()
    while True:
        main()
    