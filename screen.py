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

def loading():
    terminal_size = os.get_terminal_size()
    column_value = terminal_size.columns

    a_1=text2art("     sudosu")
    a_2=text2art("    sudosuu")
    a_3=text2art("   sudosuuu")
    a_4=text2art("  sudosuuuu")
    pr=text2art("     presente")

    ac_1=a_1.center(70)
    ac_2=a_2.center(30)
    ac_3=a_3.center(30)
    ac_4=a_4.center(30)
    pr2=pr.center(int((column_value/2)))

    os.system("cls")
    print(ac_1)
    print(pr2)
    time.sleep(1)
    os.system('cls')
    print("""   
    _____ __  ______  ____  _____ __  ____  __
    / ___// / / / __ \/ __ \/ ___// / / / / / /
    \__ \/ / / / / / / / / /\__ \/ / / / / / / 
    ___/ / /_/ / /_/ / /_/ /___/ / /_/ / /_/ /  
    /____/\____/_____/\____//____/\____/\____/   
                                            """)
    time.sleep(1)
    os.system('cls')
    print("""   
    _____ __  ______  ____  _____ __  ____  ____  __
    / ___// / / / __ \/ __ \/ ___// / / / / / / / / /
    \__ \/ / / / / / / / / /\__ \/ / / / / / / / / / 
    ___/ / /_/ / /_/ / /_/ /___/ / /_/ / /_/ / /_/ /  
    /____/\____/_____/\____//____/\____/\____/\____/   
                                                """)
    time.sleep(1)
    os.system('cls')
    print("""   
    _____ __  ______  ____  _____ __  ____  ____  ____  __
    / ___// / / / __ \/ __ \/ ___// / / / / / / / / / / / /
    \__ \/ / / / / / / / / /\__ \/ / / / / / / / / / / / / 
    ___/ / /_/ / /_/ / /_/ /___/ / /_/ / /_/ / /_/ / /_/ /  
    /____/\____/_____/\____//____/\____/\____/\____/\____/   
                                                        """)
    time.sleep(1)
    os.system("cls")

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

def title():
    #loading()
    startup()

def test(): 
    pass
    # test="Hello World !"
    # test_c=test.center(30)
    # print(test_c)


    # os.system('cls')
    # print("""   
    # _____ __  ______  ____  _____ __  __
    # / ___// / / / __ \/ __ \/ ___// / / /
    # \__ \/ / / / / / / / / /\__ \/ / / / 
    # ___/ / /_/ / /_/ / /_/ /___/ / /_/ /  
    # /____/\____/_____/\____//____/\____/   
    #                                 """)
    # time.sleep(1)
    # os.system('cls')
    # print("""   
    # _____ __  ______  ____  _____ __  ____  __
    # / ___// / / / __ \/ __ \/ ___// / / / / / /
    # \__ \/ / / / / / / / / /\__ \/ / / / / / / 
    # ___/ / /_/ / /_/ / /_/ /___/ / /_/ / /_/ /  
    # /____/\____/_____/\____//____/\____/\____/   
    #                                         """)
    # time.sleep(1)
    # os.system('cls')
    # print("""   
    # _____ __  ______  ____  _____ __  ____  ____  __
    # / ___// / / / __ \/ __ \/ ___// / / / / / / / / /
    # \__ \/ / / / / / / / / /\__ \/ / / / / / / / / / 
    # ___/ / /_/ / /_/ / /_/ /___/ / /_/ / /_/ / /_/ /  
    # /____/\____/_____/\____//____/\____/\____/\____/   
    #                                             """)
    # time.sleep(1)
    # os.system('cls')
    # print("""   
    # _____ __  ______  ____  _____ __  ____  ____  ____  __
    # / ___// / / / __ \/ __ \/ ___// / / / / / / / / / / / /
    # \__ \/ / / / / / / / / /\__ \/ / / / / / / / / / / / / 
    # ___/ / /_/ / /_/ / /_/ /___/ / /_/ / /_/ / /_/ / /_/ /  
    # /____/\____/_____/\____//____/\____/\____/\____/\____/   
    #                                                     """)
    # time.sleep(1)
    # os.system('cls')

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

def print_game_over2():
    sound_game_over()
    game_text = "GAME"
    over_text = "OVER!"
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    padding_top = (height - 1) // 2
    game_padding_left = 0
    over_padding_left = width - len(over_text)
    while game_padding_left <= (width - len(game_text)) // 2 or over_padding_left >= (width - len(over_text)) // 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" * padding_top)
        print(" " * game_padding_left + game_text, end='')
        print(" " * over_padding_left + over_text, end='')
        game_padding_left += 2
        over_padding_left -= 2
        time.sleep(0.02)
    time.sleep(6)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("game over".center(width))

if __name__ == "__main__":
    story()
    #print_game_over()


                                                               
                                                               