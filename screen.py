import os
import time
from art import *
from rich import *
import sys
import signal
from sounds import *
import pyfiglet
from rich.prompt import Prompt
from caracter import *

def wait_input():
    print("\n[italic]Appuyez sur Entrée pour continuer ...[italic]")
    input()
    sound_ok()
    time.sleep(1)
    os.system("cls")

def wait_input_turn():
    print("\n[italic]Appuyez sur Entrée pour passer au tour suivant ...[italic]")
    input()

def wait_input_pass():
    print("\n[italic]Appuyez sur Entrée pour continuer ...[italic]")
    input()
    sound_ok()
    time.sleep(1)

def wait_input_blank():
    input()
    sound_ok()
    time.sleep(1)

def stats(self):
    os.system("cls")
    tprint(f"STATS DE {self.name}")
    print(f"ATK : {self.attack_value} ⚔️ / DEF : {self.defense_value}🛡️ / VIT : {self.vitesse}⚡️\n")
    Character.show_health(self)
    Character.show_xp(self)
    wait_input()

def startup():
    os.system("cls")
    sound_startup()
    tprint("               SudoQuest")
    time.sleep(2.5)
    tprint("                           le jeu")
    time.sleep(3)
    wait_input()
    quit_pygame()

def story():
    os.system("cls")
    tprint("SUDOQUEST\n")
    histoire2 = ("Le but est de s'aventurer dans le mystérieux Sudo-Quest en utilisant les commandes du jeu.; Les donjons sont rempli d'événements aléatoires comme des coffres, des pièges et des combats avec des monstres féroces.; Les ennemis incluent des créatures terrifiantes telles que les Vermines Rampantes, les Rôdeurs des Ombres, les Serpents Venimeux, les Scorpions Tueurs et les Horreurs Abyssales, ainsi que des boss redoutables tels que le Kraken et le Dragon.; Le joueur doit améliorer les compétences de son personnage en attribuant des points à ses points de vie, ses attaques et ses défenses et collecter de l'or pour acheter de nouvelles armes et armures pour devenir le héros légendaire plong'éco de cette quête fantastique.")
    histoire = ("Bienvenue dans la mystérieuse aventure Sudo-Quest, où une grande aventure vous attend !; Vous êtes un courageux aventurier, prêt à affronter les dangers et les défis qui se trouvent dans les profondeurs de ce labyrinthe obscur.; Vous aurez la possibilité de créer votre propre personnage en choisissant parmi quatre classes distinctes :;     Mage, Voleur, Warrior ou Looser.; Chaque classe a ses propres compétences et attributs uniques, ce qui influencera votre style de jeu et votre approche des combats.; Le donjon est rempli d'événements aléatoires qui pimenteront votre aventure :; Vous pourrez tomber sur des coffres remplis de richesses, des pièges sournois qui vous causeront des blessures, ou encore des monstres féroces.; Les combats sont intenses et vous devrez utiliser vos compétences et votre stratégie pour vaincre vos ennemis et protéger votre vie.; Parmi les ennemis que vous rencontrerez, il y aura des créatures terrifiantes telles que :;     Les Vermines Rampantes, les Rôdeurs des Ombres, les Serpents Venimeux, les Scorpions Tueurs et les Horreurs Abyssales.; Et attention aux terribles boss qui vous défieront, comme le Kraken et le Dragon !; En progressant dans le donjon, vous pourrez améliorer les compétences de votre personnage en vous attribuant des points de caractéristique.; Vous pourrez également collecter de l\'or pour acheter de nouvelles armes et armures, et constituer un inventaire d\'objets puissants pour vous aider !; Attention, chaque décision que vous prendrez dans le donjon Sudo peut avoir des conséquences sur votre aventure, choisissez sagement !; Préparez-vous à une aventure épique dans un monde médiéval rempli de mystères, de trésors et de dangers et devenez un héros !; Que la chance vous accompagne, brave aventurier, dans votre quête pour conquérir le Sudo-Quest et accomplir votre destinée !; Utilisez help en jeu pour obtenir la liste des commandes disponibles.")
    string = histoire2.replace("; ", "\n\n")

    for letter in string:
        print(letter, end="")
        time.sleep(0.005)
    wait_input_blank()

def over():
    quit_pygame()
    time.sleep(3)
    signal.signal(signal.SIGINT, over)
    sound_game_over()
    tprint("GAME OVER !!")
    #sys.stdout.flush()
    time.sleep(5)
    fin = input("Rejouer ? (Oui/Non)")
    if fin.lower().startswith("o"):
        pass
    else :
        exit(0)

def end_stats(self):
    os.system("cls")
    tprint("GAME OVER")
    print(f"STATISTIQUES DE LA PARTIE DE {self.name} :\nClasse : {self.type}\n")
    print(f"\nVous avez vaincu {self.kills} ennemis !\nVotre plus long combat à duré {self.tours_max} tours !\nVOus avez one-tap {self.OHKO} ennemis !\nVous avez ouvert {self.chests} coffres !\nVous avez accumulé {self.gold} or !\nVous avez \"exploré\" {self.steps} fois !\nVous êtes tombé dans {self.traps} pièges !\n")
    fin = input("\nRejouer ? (Oui/Non)")
    if fin.lower().startswith("o"):
        pass
    else :
        exit(0)

def print_game_over():
    quit_pygame()
    sound_game_over()
    text = "GAMEOVER!"

    for char in text:
        # ascii_art = pyfiglet.figlet_format(char)
        # print(ascii_art, end='')
        print(char, end="")
        time.sleep(0.5)
    time.sleep(2)                                                      
                                                               