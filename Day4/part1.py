#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 4
Part : 1

Ce script identifie tous les rouleaux de papier accessibles. 
Un rouleau '@' est considéré accessible si moins de quatre de ses 
huit voisins adjacents sont également des '@'.

Le résultat correspond au nombre total de rouleaux accessibles 
dans l'état initial du schéma.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Constantes
NEIGHBORS: list = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0), (1, 1)    
]
# ===========================================================================

# %% ========================================================================
# Input data
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'input pour le jour donné.

    :param day: numéro du jour AOC
    :param example: si True, utilise le fichier example.txt sinon input.txt
    :return: liste de lignes du fichier
    :rtype: list
    """
    file = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{file}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data: list) -> int:
    """
    Détermine le nombre de rouleaux accessibles dans la grille initiale.
    Un rouleau est accessible si moins de quatre de ses huit voisins 
    sont également des '@'.

    :param data: Liste brute des lignes d’input.
    :return: Nombre total de rouleaux accessibles.
    :rtype: int
    """
    paper_rolls  = set()
    accessible_roll_count  = 0

    # Collecte des positions '@'
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "@":
                paper_rolls .add((y, x))

    # Comptage des rouleaux accessibles
    for (y, x) in paper_rolls :
        neighbor_count  = 0
        for dy, dx in NEIGHBORS:
            neighbor = (y + dy, x + dx)
            if neighbor in paper_rolls :
                neighbor_count  += 1

        if neighbor_count  < 4:
            accessible_roll_count += 1

    return accessible_roll_count

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(4, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 4 | Part 1".center(60))
    print("═" * 60)
    print(f"Rouleaux accessibles : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
