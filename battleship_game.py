#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Définition des navires pour le jeu de bataille navale.

Chaque navire est un dictionnaire où :
- Les clés sont des tuples qui représentent les coordonnées du navire sur la grille de jeu.
- Les valeurs sont des booléens qui indiquent si la partie du navire à ces coordonnées a été touchée ou non.

:return: Un dictionnaire représentant un navire.
"""


def ask_coord():
    """
    Demande au joueur d'entrer les coordonnées d'un tir.

    Returns:
        tuple: Les coordonnées du tir sous forme de tuple (lettre, chiffre).
    """
    while True:
        coord = input("Entrez les coordonnées de votre tir (ex. : A1) : ")
        try:
            if not coord[0].isalpha():
                raise ValueError  # Déclenche une exception ValueError
            letter = coord[0].upper()

            number = int(coord[1:])
            return (letter, number)
        except ValueError:
            print("Veuillez entrer une lettre suivie d'un nombre.")
        except IndexError:
            print("Veuillez entrer au moins une lettre et un nombre pour la coordonnée.")


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
    start_letter, start_number = start_coord
    for i in range(size):
        if orientation == "H":
            # Augmente la lettre pour l'orientation horizontale
            ship[(chr(ord(start_letter) + i), start_number)] = False
        else:
            # Augmente le nombre pour l'orientation verticale
            ship[(start_letter, start_number + i)] = False
    ships[name] = ship


ships = {}
create_ship(ships, "Porte-avions", ("B", 2), 5, "H")
create_ship(ships, "Croiseur", ("A", 4), 4, "V")
create_ship(ships, "Contre-torpilleur", ("C", 5), 3, "V")
create_ship(ships, "Sous-marin", ("E", 9), 2, "H")
create_ship(ships, "Torpilleur", ("H", 5), 3, "H")

# Contenu des dictionnaires
for i, (name, ship) in enumerate(ships.items(), start=1):
    print(f"Navire {i}: {name} {ship}")


def ship_is_hit(ship, shot_coord):
    """
    Vérifie si un navire est touché par un tir.

    Args:
        ship (dict): Le navire à vérifier.
        shot_coord (tuple): Les coordonnées du tir.

    Returns:
        bool: True si le navire est touché, False sinon.
    """
    return shot_coord in ship


def ship_is_sunk(ship):
    """
    Vérifie si un navire est coulé.

    Args:
        ship (dict): Le navire à vérifier.

    Returns:
        bool: True si le navire est coulé, False sinon.
    """
    return all(ship.values())


def analyze_shot(ships, name, shot_coord):
    """
    Analyse un tir sur un navire.

    Args:
        ships (dict): Dictionnaire contenant les navires.
        name (str): Nom du navire.
        shot_coord (tuple): Les coordonnées du tir.

    Returns:
        bool: True si le navire a été touché par le tir, False sinon.
    """
    ship = ships[name]
    if ship_is_hit(ship, shot_coord):
        print("Touché !")
        ship[shot_coord] = True
        if ship_is_sunk(ship):
            print("Coulé !")
            del ships[name]
        return True
    return False


# Boucle de jeu
while True:
    # Entrée de l'utilisateur
    shot = ask_coord()  # Obtenir les coordonnées du tir

    # Contrôler le formatage du tir
    print(shot)

    # Tir a touché un navire
    for name in list(ships.keys()):
        if analyze_shot(ships, name, shot):
            break
    else:
        print("Manqué !")

    # Jeu terminé
    if not ships:
        print("Vous avez gagné !")
        break
