#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Définition des navires pour le jeu de bataille navale.

Chaque navire est un dictionnaire où :
- Les clés sont des tuples qui représentent les coordonnées du navire sur la grille de jeu.
- Les valeurs sont des booléens qui indiquent si la partie du navire à ces coordonnées a été touchée ou non.

:return: Un dictionnaire représentant un navire.
"""

# Porte-avion en B2 à B6
aircraft_carrier = {
    ("B", 2): False,
    ("B", 3): False,
    ("B", 4): False,
    ("B", 5): False,
    ("B", 6): False,
}

# Croiseur en A4 à A7
cruiser = {("A", 4): False, ("A", 5): False, ("A", 6): False, ("A", 7): False}

# Contre-torpilleur en C5 à C7
destroyer = {("C", 5): False, ("C", 6): False, ("C", 7): False}

# Sous-marin en H5 à H7
submarine = {("H", 5): False, ("H", 6): False, ("H", 7): False}

# Torpilleur en E9 à E10
torpedo_boat = {("E", 9): False, ("E", 10): False}

# Liste de tous les navires
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

# Contenu des dictionnaires
for i, ship in enumerate(ships_list, start=1):
    print(f"Navire {i}: ", ship)
