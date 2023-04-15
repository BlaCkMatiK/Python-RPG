import os
import time
from art import *
from rich import *
import sys
import signal
from sounds import *
import pyfiglet

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
    tprint("                      le jeu")
    time.sleep(3)
    print("Appuyez sur Entrée pour continuer ...")
    input("")
    quit_pygame()

def menu():
    pass

def title():
    #loading()
    startup()

def story():
    pass

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
    print(f"\nVous avez vaincu {self.kills} ennemis !\nVotre plus long combat à duré {self.tours_max} tours !\nVOus avez one-tap {self.OHKO} enemis !\nVous avez ouvert {self.chests} coffres !\nVous avez accumulé {self.gold} or !\nVous avez \"exploré\" {self.steps} fois !\nVous êtes tombé dans {self.traps} pièges !\n")
    fin = input("\nRejouer ? (Oui/Non)")
    if fin.lower().startswith("o"):
        pass
    else :
        exit(0)

def print_game_over():
    quit_pygame()
    sound_game_over()
    text = "game over"

    for char in text:
        ascii_art = pyfiglet.figlet_format(char)
        print(ascii_art, end='')
        time.sleep(0.5)
    time.sleep(2)

def print_game_over2():
    sound_game_over()
    game_text = "game"
    over_text = "over"
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
    print_game_over()


                                                               
                                                               