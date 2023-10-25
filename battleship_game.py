#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Définition des navires pour le jeu de bataille navale.

Chaque navire est un dictionnaire où :
- Les clés sont des tuples qui représentent les coordonnées du navire sur la grille de jeu.
- Les valeurs sont des booléens qui indiquent si la partie du navire à ces coordonnées a été touchée ou non.

:return: Un dictionnaire représentant un navire.
"""


def create_ship(ships, name, start_coord, size, orientation):
    """
    Crée un navire à partir d'un nom, d'une coordonnée de départ, d'une taille et d'une orientation, et l'ajoute au dictionnaire ships.

    Args:
        ships (dict): Dictionnaire contenant les navires.
        name (str): Nom du navire.
        start_coord (tuple): Coordonnée de départ du navire.
        size (int): Nombre de cases du navire.
        orientation (str): Orientation du navire ("H" pour horizontal, "V" pour vertical).
    """
    ship = {}
    for i in range(size):
        if orientation == "H":
            ship[(start_coord[0], start_coord[1] + i)] = False
        else:
            ship[(chr(ord(start_coord[0]) + i), start_coord[1])] = False
    ships[name] = ship


ships = {}
create_ship(ships, "Porte-avions", ("B", 2), 5, "H")
create_ship(ships, "Croiseur", ("A", 4), 4, "V")
create_ship(ships, "Contre-torpilleur", ("C", 5), 3, "H")
create_ship(ships, "Sous-marin", ("H", 5), 3, "H")
create_ship(ships, "Torpilleur", ("E", 9), 2, "H")

# Contenu des dictionnaires
for i, (name, ship) in enumerate(ships.items(), start=1):
    print(f"Navire {i}: {name} {ship}")

# Boucle de jeu
while True:
    # Entrée de l'utilisateur
    shot = input("Entrez les coordonnées de votre tir (ex. : A1) : ")

    try:
        # Convertit l'entrée en tuple (lettre, nombre)
        shot = (shot[0].upper(), int(shot[1:]))
    except ValueError:
        # Si l'entrée est invalide, affiche un message et recommence la boucle
        print("Coordonnées non valides. Veuillez réessayer.")
        continue

    # Contrôler le formatage du tir
    print(shot)

    # Vérifier si le tir a touché un navire
    for ship in ships.values():
        if shot in ship:
            print("Touché !")
            ship[shot] = True

            # Vérifier si le navire est coulé
            if all(ship.values()):
                print("Coulé !")

            break
    else:
        print("Manqué !")

       # Vérifier si le jeu est terminé
    if all(all(ship.values()) for ship in ships.values()):
        print("Vous avez gagné !")
        break
