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

# Boucle de jeu
while True:
    # Entrée de l'utilisateur
    shot = ask_coord()  # Utilisez la fonction ask_coord pour obtenir les coordonnées du tir

    # Contrôler le formatage du tir
    print(shot)

    # Vérifier si le tir a touché un navire
    for ship in ships.values():
        if shot in ship:
            if ship[shot] == True:
                print("Cette partie du navire a déjà été touchée !")
            else:
                ship[shot] = True
                if all(ship.values()):
                    print("Coulé !")
                else:
                    print("Touché !")
            break
    else:
        print("Manqué !")

    # Vérifier si le jeu est terminé
    if all(all(ship.values()) for ship in ships.values()):
        print("Vous avez gagné !")
        break
