import random

from caracter import *
from screen import *
from inventaire import *
from combat import Combat
from items import *
from inventaire import *

class Event:
    def __init__(self, player, equip):
        self.player = player
        self.equip = equip

    def explore(self, player, equip):
        events_list = [
            ("vide"),
            ("coffre"),
            ("monstre"),
            ("magasin"),
            ("piege"),
            ("couloir"),
        ]
        events_prob = [0.1, 0.2, 0.4, 0.1, 0.1, 0.1]

        event = self._choix_pondéré(events_list, events_prob)

        if event == "vide":
            self.salle_vide(player, equip)
        elif event == "coffre":
            self.salle_coffre(player, equip)
        elif event == "monstre":
            self.salle_monstre(player, equip)
        elif event == "magasin":
            self.salle_magasin(player, equip)
        elif event == "piege":
            self.salle_piege(player, equip)
        elif event == "couloir":
            self.salle_couloir(player, equip)

    def salle_vide(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        Entree(f"Ouf ! {player.name} trouve une salle vide", '> ', True).run()

    def salle_coffre(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print("Vous avez trouvé un coffre !")
        if Entree("Voulez-vous l'ouvrir ? (Oui/Non)", "> ").lower().startswith("o"):
            sound_chest_o()
            print("\nLe coffre s'ouvre")
            for i in range(0, 3):
                time.sleep(0.5)
                print(".")
            """ Fonction qui retourne un item aléatoire parmi une arme, une armure ou de l'or """
            item_1 = random_arme()
            item_2 = random_armure()
            item_3 = random_potion()
            items = [item_1, item_2, item_3]
            item_choisi = choice(items)
            if item_choisi == item_1:
                equip.ajouter_arme(player, item_choisi)
                print(f"\nVous obtenez {item_choisi.name}")
            elif item_choisi == item_2:
                equip.ajouter_armure(player, item_choisi)
                print(f"\nVous obtenez {item_choisi.name}")
            elif item_choisi == item_3:
                equip.ajouter_potion(player, item_choisi)
                print(f"\nVous obtenez {item_choisi.name}")
            else:
                quantite_or = random.randint(1, 10)
                equip.ajouter_or(player, quantite_or)
            sound_item()
            time.sleep(2)
            print("\nVous fermez le coffre\n")
            sound_chest_c()
            player.chests +=1
            Entree("[italic]Appuyez sur entrée pour continuer ...[italic]","", True).run()
        else:
            Entree("Vous n'avez pas ouvert ce coffre.", "> ", True).run()
     
    def salle_monstre(self, player, equip, niveau="base"):
        os.system("cls")
        tprint("COMBAT")
        time.sleep(0.1)
        quit_pygame()
        sound_battle()
        print("%s rencontre %s" % (player.name, 'un ennemi !'))
        player.status = "combat"
        while True:
            if niveau == "boss":
                    enemy = random_boss()
                    battle = Combat(player, equip, enemy)
                    battle.battle(player, equip, enemy)
                    break
            a = Entree("Voulez-vous tenter de fuir? (Oui / Non)", "> ").run()
            if a.lower().startswith("o"):
                        if randint(0, 1) == 1 :
                            quit_pygame()
                            sound_fuite()
                            time.sleep(2)
                            Entree("Vous avez réussi à fuire !", "> ").run()
                            sound_bgm()
                            Event(player, equip).salle_vide(player, equip)
                            break
                        else:
                            Entree("Vous n'avez pas réussi à fuire !","> ").run()
            player.status = "combat"
            enemy = random_enemy()
            battle = Combat(player, equip, enemy)
            battle.battle(player, equip, enemy)
            break               

    def salle_magasin(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print("Il y a un marchand !")
        choix=Entree("Rentrer dans le magasin ? (Oui/Non)", "> ")
        if choix.lower().startswith("o"):
            quit_pygame()
            print("Vous entrez dans le magasin")
            sound_marchand()
            time.sleep(2)
            os.system("cls")
            tprint("MARCHAND")
            sound_shop()
            # variable var_1 qui est un nombre random entre 1 et 3
            var_1 = randint(1, 3)
            if var_1 == 1:
                print("Bonjour marchand certifié sudosu pour vous servir, Que voulez-vous aujourd'hui ?")
            elif var_1 == 2:
                print("Bonjour aventurier quel bien vous ferez plaisir aujourd'hui ?")
            else:
                    print("C'est quelle heure pour acheter du materiel chef ?")
            choix=Entree("\n1. Arme ⚔️ \n2. Armure 🛡️ \n3. Soin ❤️\n\nQu'est-ce qui vous intéresse ?", "> ").run()

            #Arme
            if choix.lower().startswith("1"):
                os.system("cls")
                tprint("MARCHAND - ARMES")
                ct = 0
                print(f"Vous avez [yellow]{player.gold} or[yellow]\n")
                for arme in armes_list:
                    ct +=1
                    print(f"{ct}. {arme.name} / + {arme.bonus} ATK / [yellow]{arme.price} or[yellow]\n")
                if player.armes == []:
                    choix =Entree(f"Que voulez vous acheter ? / (Actuellement vous n'avez pas d'arme)", "> ").run()
                else:
                    choix=Entree(f"Que voulez vous acheter ? / Actuellement vous avez [purple]{player.armes[0].name}[purple]", "> ").run()
                try:
                    choix = int(choix)
                    choix = armes_list[choix-1]                    
                    equip.achat(player, choix)
                except (ValueError, IndexError):
                    Entree("Vous n'avez rien acheté", "> ", True).run()

            #Armure
            elif choix.lower().startswith("2"):
                os.system("cls")
                tprint("MARCHAND - ARMURES")
                ct = 0
                print(f"Vous avez [yellow]{player.gold} or[yellow]")
                for armure in armures_list:
                    ct+=1
                    print(f"{ct}. {armure.name} / + {armure.bonus} ATK / [yellow]{armure.price} or[yellow]\n")
                if player.armures == []:
                    choix =Entree(f"Que voulez vous acheter ? / (Actuellement vous n'avez pas d'armure)", "> ").run()
                else:
                    choix=Entree(f"Que voulez vous acheter ? / Actuellement vous avez {player.armures[0].name}", "> ").run()
                choix=Entree("Que voulez vous acheter ?", "> ").run()
                try:
                    choix = int(choix)
                    choix = armures_list[choix-1]                    
                    equip.achat(player, choix)
                except (ValueError, IndexError):
                    Entree("Vous n'avez rien acheté", "> ", True).run()

            #Soins
            else:
                os.system("cls")
                tprint("MARCHAND - SOINS")
                ct = 0
                print(f"Vous avez [yellow]{player.gold} or[yellow]")
                for potion in potions_list:
                    ct+=1
                    print(f"{ct}. {potion.name} / + {potion.bonus} ATK / [yellow]{potion.price} or[yellow]\n")  
                try:
                    choix = int(choix)
                    choix = potions_list[choix-1]                    
                    equip.achat(player, choix)
                except (ValueError, IndexError):
                    Entree("Vous n'avez rien acheté", "> ", True).run()
            
            quit_pygame()
            sound_bgm()
        else:
            var_2 = randint(1, 1000)
            if var_2 >= 1 and var_2 <= 300:

                print("Aurevoir cher ami !")
            elif var_2 >= 301 and var_2 <= 600:
                print("Bonne journée en esperant vous revoir au plus vite")
            elif var_2 >= 601 and var_2 <= 999:
                print("Le marchant vous souhaite une bonne journée !")
            elif var_2 == 1:
                print("Oh le rat")
        Entree("\n[italic]Appuez sur entrée pour continuer ... [italic]", "", True).run()

    def salle_piege(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print("Tout est très calme dans cette pièce...")
        for i in range(0, 3):
            time.sleep(1)
            print(".")
        time.sleep(1)
        print("\nAie ! Vous venez de vous prendre un piège!")
        sound_trap()
        time.sleep(1)
        trap = randint(1,2)
        Entree(f"Vous avez perdu {trap*2} HP ❤️ ", "> ", True)
        player.health -= 2
        player.traps +=1
    
    def salle_couloir(self, player, equip):
        os.system("cls")
        tprint("SALLE")
        print(f"{player.name} avance dans un couloir très étroit")
        for i in range(0, 3):
            time.sleep(1)
            print(".")
        a = randint(0, 10)
        if a  <=6 :
            Entree("Il y a un boss !", "> ", True).run()
            Event(player, equip).salle_monstre(player, equip, "boss")
        elif a > 6 and a < 8 :
            Event(player, equip).salle_coffre(player, equip)
        else : 
            Event(player, equip).salle_magasin(player, equip)

    def _choix_pondéré(self, list, prob):
        """Choix pondéré d'un évenement

        Args:
            list (list): nom evenements
            prob (list): probabilités
        """
        return choices(list, prob)[0]