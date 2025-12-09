#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent of Code 2025
===================
Day : 9
Part : 2

Ce script calcule la plus grande aire d’un rectangle axis-aligné totalement
contenu dans une boucle décrite par une liste de points (x,y).

L’algorithme utilisé est une version optimisée (O(N²)) :
- on parcourt toutes les paires de points,
- on calcule le rectangle correspondant,
- on vérifie rapidement s’il est entièrement contenu dans la boucle,
- on garde le maximum.

La vérification s’appuie sur les segments de la boucle (edges), ce qui évite
les bibliothèques lourdes comme shapely tout en restant efficace.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ======================================================================== 
# Import
from itertools import combinations

# ===========================================================================

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
        return f.read().strip()
# ===========================================================================

# %% ========================================================================
# Fonctions utilitaires
def calculate_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """
    Calcule l’aire d’un rectangle défini par deux coins.

    Les deux coins sont inclus → +1 sur chaque dimension.

    :param p1: premier point (x, y)
    :param p2: second point (x, y)
    :return: aire du rectangle
    :rtype: int
    """
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

# ---------------------------------------------------------------------------
def is_fully_contained(
    edges: list[tuple[int, int, int, int]],
    min_x: int,
    min_y: int,
    max_x: int,
    max_y: int,
) -> bool:
    """
    Vérifie si un rectangle est entièrement contenu dans la boucle.

    On teste si le rectangle coupe un des segments :
    - si oui → il n’est pas contenu,
    - sinon → il est contenu.

    :param edges: segments de la boucle (min_x, min_y, max_x, max_y)
    :param min_x: borne gauche du rectangle
    :param min_y: borne basse
    :param max_x: borne droite
    :param max_y: borne haute
    :return: True si contenu, False sinon
    :rtype: bool
    """
    for e_min_x, e_min_y, e_max_x, e_max_y in edges:
        # intersection stricte avec un segment → rectangle "sort"
        if min_x < e_max_x and max_x > e_min_x and min_y < e_max_y and max_y > e_min_y:
            return False

    return True

# ===========================================================================

# %% ========================================================================
# Résolution — Partie 2 optimisée
def solve(data: str) -> int:
    """
    Calcule la plus grande aire contenue dans la boucle.

    Étapes :
    1. Parser les points,
    2. Construire les segments,
    3. Tester toutes les paires,
    4. Vérifier la containment,
    5. Garder le maximum.

    :param data: texte brut des points "x,y"
    :return: aire maximale trouvée
    :rtype: int
    """
    # parse des points
    tiles = [
        (int(x), int(y))
        for line in data.splitlines()
        for (x, y) in [line.split(",")]
    ]

    n = len(tiles)

    # construction des segments (edges)
    edges = []
    for i in range(n - 1):
        p1, p2 = tiles[i], tiles[i + 1]
        edges.append(
            (min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1]))
        )

    # segment final (boucle)
    p_last = tiles[-1]
    p_first = tiles[0]
    edges.append(
        (
            min(p_last[0], p_first[0]),
            min(p_last[1], p_first[1]),
            max(p_last[0], p_first[0]),
            max(p_last[1], p_first[1]),
        )
    )

    best = 0

    # test toutes les paires
    for p1, p2 in combinations(tiles, 2):

        area = calculate_area(p1, p2)

        # prune → inutile de tester les petites aires
        if area <= best:
            continue

        min_x, max_x = sorted((p1[0], p2[0]))
        min_y, max_y = sorted((p1[1], p2[1]))

        # containment
        if is_fully_contained(edges, min_x, min_y, max_x, max_y):
            best = area

    return best

# ======================================================================

# %% ========================================================================
# Programme principal
if __name__ == "__main__":
    INPUT = get_input(9, False)
    RESULT = solve(INPUT)

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 9 | Part 2".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")

# ===========================================================================