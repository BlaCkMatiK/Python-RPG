# SudoQuest

![image info](./img/logo.png)

SudoQuest est un rogue-like en ligne de commandes codé en Python.

## L'équipe

Il est développé par l'équipe Sudo-su composée de :  
Sébastien ABELA  
Thomas BREMARD  
Matteo DECOUT  
Romain IGOUNET  
Mateo LALANNE DE MIRAS  
Grégoire SEGUIN  

## Le jeu

### Prérequis

Le jeu à été développé sous Python 3.11 .

SudoQuest nécessite certaines libraires de Python pour fonctionner :

```sh
pip install rich pygame pyfiglet art
```

A l'heure actuelle, le fichier **engine.py** doit être exécuté depuis un terminal.

```sh
python engine.py
```

Nous essayerons de compiler proprement le jeu pour le transformer en **.exe**

### Principe

Le joueur crée son personnage en choisissant une classe et en attribuant un certain nombre de points de compétences dans différentes catégories (hp, atk, def).  
Il peut inscrire des commandes dans la console qui lui permettront de s'aventurer dans le mystérieux donjon Sudo …

### Systèmes

Actuellement, le joueur peut explorer le donjon. Aléatoirement, il peut rencontrer des évènements comme des coffres, des pièges ou des combats. Ces derniers sont contre des monstres aléatoires qui, une fois vaincus, donnent or, armes et armures.

### Commandes

explore (permet d'avancer dans le donjon)  
hp (permet de connaitre ses points de vie actuels)  
combat (permet de choisir de combattre un ennemi rencontré)  
fuite (permet de fuir ce combat)  
inventaire (permet d'afficher son inventaire)  

## Mises à jour éventuelles

Ci dessous, une feuille de route de nos mises à jour.

### Must

Un écran titre ✔️  
Un écran de Game Over ⏳  
Différents monstres ✔️  
Choix de couloirs  

### Should

Equipement  
Expérience / Niveaux => Ennemis + puissants

### Could

Affixes (Bonus par armes sur classes, ...)  
Magasin d'achat d'items  

### Would

Des sons d'ambiance ✔️  
Un meilleur affichage ⏳  
Sauvegarde + Tableau des scores  
Joueurs AI  
Sorts et compétences par gain d'XP  
