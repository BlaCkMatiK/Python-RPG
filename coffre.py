import random
from caracter import ajouter_arme, ajouter_armure, ajouter_or

def ouvrir_coffre():
    """ Fonction qui retourne un item aléatoire parmi une arme, une armure ou de l'or """
    items = ["arme", "armure", "or"]
    item_choisi = random.choice(items)
    if item_choisi == "arme":
        return "Vous avez trouvé une arme !"
        car1.ajouter_arme
    elif item_choisi == "armure":
        return "Vous avez trouvé une armure !"
        car1.ajouter_armure
    else:
        quantite_or = random.randint(1, 10)
        return f"Vous avez trouvé {quantite_or} pièces d'or !"
        car1.ajouter_or

