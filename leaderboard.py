import requests
from requests.exceptions import RequestException
from screen import Entree

def send_to_leaderboard(player):

    level = player.level
    classe = player.type
    steps = player.steps
    kills = player.kills
    
    #print("\nLe Leaderboard peut être consulté à l'adresse : https://sudo-su.fr/sudoquest/lead.php !")
    if Entree("\nEnvoyer le score dans le leaderboard ? (Oui/Non) (Consultable à https://sudo-su.fr/sudoquest/lead.php )", "> ").run().lower().startswith("o"):
        name = Entree("\nQuel est votre nom de joueur ?", "> ").run()
        data = {'player_name': name}
        url = 'http://sudo-su.fr:5000/receive_score'
        response = requests.post(url, data=data)
        
        if 'present' in response.text:
            Entree("\aAh ! Un score a déjà été enregistré pour ce joueur.\n[italic]Appuyez sur Entrée pour continuer ...[italic]", "").run()
            while True:
                #a = input("Voulez vous modifier ce score ? (o/n)")
                if Entree("Voulez vous modifier ce score ? (Oui/Non) \n[bold][red]Attention ! Le score précédent sera écrasé ![red][bold]", "> ").run().lower().startswith("o"):
                    p = Entree("\nEntrez votre Passphrase", "> ").run()
                    url = "http://sudo-su.fr:5000/update_score"
                    data = {"player_name":name, "level":level, "passphrase": p, "class":classe, "steps":steps, "kills":kills}
                    response = requests.post(url, data=data)
                    if response.status_code == 200:
                        Entree(response.text, "").run()
                        break
                    else:
                        Entree(response.text, "").run()
                else :
                    break
        else:
            Entree("\nAucun score associé à ce nom de joueur !\n[italic]Appuyez sur Entrée pour continuer ...[italic]", "").run()
            p = Entree("\nDéfinissez une Passphrase (Utilisée pour modifier vos prochains meilleurs scores)", "> ").run()
            url = 'http://sudo-su.fr:5000/insert_score'
            data = {"player_name":name, "level":level, "passphrase": p, "class":classe, "steps":steps, "kills":kills}
            response = requests.post(url, data=data)
            Entree(response.text, "").run()
        #print("\nLe Leaderboard peut être consulté à l'adresse : https://sudo-su.fr/sudoquest/lead.php !")
    else:
        pass
        #print(f"\nDésolé, une erreur est survenue dans l'envoi de votre score :", response.text)