import os
import time
from art import *
from rich import *
import winsound

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


def menu():
    winsound.PlaySound('sounds/title.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )
    tprint("               SudoQuest")
    tprint("                      le jeu")
    time.sleep(5)
    print("Appuyez sur Entrée pour continuer ...")
    input("")
    winsound.PlaySound(None, winsound.SND_ASYNC)

def title():
    loading()
    menu()
    
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
    print("GAME OVER !!")