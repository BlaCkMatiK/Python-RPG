#import rich
import os
import random
import time

from caracter import *
from dice import Dice
from evenement import *
from screen import *
import signal
import threading

def handle_signal(signal_num, frame):
    os.system("cls")
    print("Fermeture du jeu prématurée par l'utilisateur (Ctrl+C) \n3 secs. avant fermeture")
    time.sleep(3)
    exit(0)

signal.signal(signal.SIGINT, handle_signal)

def start():
    title()
    os.system("cls")

def main():    
    player = create_character()
    #stats(player)
    while Character.is_alive(player):
        choose_event(player)
    over()
    main()

if __name__ == "__main__":
    start()
    while True:
        main()
    