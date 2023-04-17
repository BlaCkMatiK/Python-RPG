#import rich
import os
import random
import time

from caracter import *
from dice import Dice
from evenement import *
from screen import startup, story
import signal
import threading
from sounds import *

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
    story()

def main():
    player = create_character()
    quit_pygame()
    sound_enter()
    time.sleep(10)
    os.system("cls")
    sound_bgm()
    #stats(player)
    while Character.is_alive(player):
        choose_event(player)
    #over()
    print_game_over()
    end_stats(player)
    main()

if __name__ == "__main__":
    start()
    while True:
        main()
    