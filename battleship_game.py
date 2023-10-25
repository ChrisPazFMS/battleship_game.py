#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
