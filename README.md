# Motus

Documentation du jeu Motus

Description:

Ce programme premet de jouer au Motus en Python. Le but du jeu est de deviner un mot secret de cinq lettres en six essais maximum.

Fonctionalitées:

Chargement d'une liste de mots: Le programme charge une liste de mots français à partir du fichier texte mots.txt. Génération aléatoire d'un mot cible: Le programme choisit un mot aléatoire dans la liste des mots chargés. Camouflage d'un mot avec des indices: Le programme affiche un mot camouflé avec des indices pour chaque lettre :

Affichage avec tkinter:

-# : la lettre n'est pas dans le mot cible. -lettre minuscule : la lettre est dans le mot cible mais mal placée. -LETTRE MAJUSCULE : la lettre est dans le mot cible et bien placée.

Validation des mots proposés: Le programme vérifie si le mot proposé par le joueur est valide (longueur, première lettre) et lui donne des indices.

Fin de la partie: La partie se termine lorsque le joueur trouve le mot cible ou après six essais infructueux. Fichiers:

motus.py: Le fichier principal du programme. data_mots.txt: Le fichier contenant la liste des mots français. Exécution:

Pour jouer au jeu, exécutez simplement le fichier motus.py dans un interpréteur Python.
