#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 7
Part : 1

Ce script simule la propagation d’un faisceau lumineux depuis un point
d’entrée marqué par 'S'. Le faisceau descend ligne par ligne.

Lorsque le faisceau rencontre un splitter '^', il :
    - compte une occurrence,
    - se divise en deux faisceaux (gauche et droite).

Les faisceaux continuent leur propagation jusqu’à la fin de la carte ou
jusqu’à ce qu’aucun faisceau ne reste actif.

Le résultat correspond au nombre total de splitters traversés.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""


# %% ========================================================================
# Input data
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée pour le jour donné.

    :param day: numéro du jour AoC
    :param example: True pour example.txt, False pour input.txt
    :return: liste des lignes du fichier
    """
    filename = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{filename}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data: list) -> int:
    """
    Simule les faisceaux descendants depuis 'S' et compte les splitters '^'.

    :param data: liste de lignes décrivant la carte
    :return: nombre total de splitters rencontrés
    """

    # Préparation des lignes
    rows = [line.rstrip("\n") for line in data]
    height = len(rows)
    if height == 0:
        return 0

    width = max(len(r) for r in rows)
    grid = [r.ljust(width, " ") for r in rows]

    # Recherche de la position de 'S'
    start_row = start_col = None
    for i, row in enumerate(grid):
        if "S" in row:
            start_row = i
            start_col = row.index("S")
            break

    if start_row is None:
        raise ValueError("Point d'entrée 'S' introuvable dans l'input")

    splits = 0

    # Faisceaux actifs (colonnes)
    active_beams = {start_col}

    # Propagation ligne par ligne
    for r in range(start_row + 1, height):
        next_beams = set()

        for c in active_beams:
            if c < 0 or c >= width:
                continue

            ch = grid[r][c]

            # Splitter : deux faisceaux + comptage
            if ch == "^":
                splits += 1
                if c - 1 >= 0:
                    next_beams.add(c - 1)
                if c + 1 < width:
                    next_beams.add(c + 1)

            else:
                # Le faisceau continue
                next_beams.add(c)

        if not next_beams:
            break

        active_beams = next_beams

    return splits

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(7, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 7 | Part 1".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
