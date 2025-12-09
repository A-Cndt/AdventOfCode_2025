#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 9
Part : 1

Ce script recherche la plus grande surface de rectangle axis-aligné
que l’on peut former à partir de deux tuiles rouges utilisées comme
coins opposés.

Chaque ligne de l’input fournit une coordonnée "x,y".
Deux points définissent un rectangle dont l’aire vaut :
    aire = |dx| * |dy|

La solution :
-------------
- lit toutes les coordonnées,
- parcourt toutes les paires de points,
- calcule l’aire associée,
- conserve la plus grande.

La complexité est O(n²), ce qui reste acceptable pour les tailles
de données de l’énoncé.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Lecture de l’input
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée pour le jour demandé.

    :param day: numéro du jour AoC
    :param example: True → example.txt, False → input.txt
    :return: liste de lignes sans fin de ligne
    """
    file = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{file}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data: list) -> int:
    """
    Calcule la plus grande aire de rectangle formé par deux points.

    :param data: lignes contenant "x,y"
    :return: aire maximale
    """
    points = []

    # Parsing des coordonnées
    for line in data:
        x, y = map(int, line.split(','))
        points.append((x, y))

    n = len(points)
    best = 0

    # Test de toutes les paires
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1

            area = width * height

            if area > best:
                best = area

    return best

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(9, False))   # True pour example, False pour input réel

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 9 | Part 1".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
