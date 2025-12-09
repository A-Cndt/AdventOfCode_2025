#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 7
Part : 2

Ce script simule la propagation de multiples faisceaux lumineux depuis un
point d’entrée 'S'. Chaque faisceau descend ligne par ligne.

Lorsqu’un faisceau rencontre un splitter '^', il :
    - se divise en deux faisceaux,
    - le nombre de faisceaux se multiplie donc.

L’objectif est de calculer le **nombre total de faisceaux arrivant en bas
de la carte**, après toutes les divisions.

La simulation conserve pour chaque colonne le nombre de faisceaux actifs,
et met à jour ces comptages à chaque ligne.

Le résultat final correspond à la somme des faisceaux restants.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Import 
from collections import defaultdict

# ===========================================================================

# %% ========================================================================
# Input data
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée pour le jour donné.

    :param day: numéro du jour AoC
    :param example: True pour example.txt, False pour input.txt
    :return: liste des lignes lues
    """
    filename = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{filename}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data: list) -> int:
    """
    Simule la descente des faisceaux depuis 'S' et compte toutes les branches.

    Chaque faisceau suit la colonne jusqu'à rencontrer '^'.
    Un splitter génère deux nouvelles branches.
    Les branches sont comptabilisées via un dictionnaire {colonne: nombre}.

    :param data: lignes décrivant la carte
    :return: nombre total de faisceaux en bas de la carte
    """

    rows = [r.rstrip("\n") for r in data]
    if not rows:
        return 0

    height = len(rows)
    width = max(len(r) for r in rows)
    grid = [r.ljust(width, " ") for r in rows]

    # Recherche du point de départ 'S'
    start_row = start_col = None
    for i, row in enumerate(grid):
        if "S" in row:
            start_row = i
            start_col = row.index("S")
            break

    if start_row is None:
        raise ValueError("Point d'entrée 'S' introuvable dans l'input")

    # current[col] = nombre de faisceaux actifs dans la colonne
    current = defaultdict(int)
    current[start_col] = 1

    # Propagation ligne par ligne
    for r in range(start_row + 1, height):
        next_state = defaultdict(int)

        for col, count in current.items():
            if count == 0:
                continue
            if col < 0 or col >= width:
                continue

            ch = grid[r][col]

            # Splitter : deux branches
            if ch == "^":
                if col - 1 >= 0:
                    next_state[col - 1] += count
                if col + 1 < width:
                    next_state[col + 1] += count

            else:
                # Le faisceau continue droit
                next_state[col] += count

        # Si plus aucun faisceau actif → fin anticipée
        if not next_state:
            current = next_state
            break

        current = next_state

    # Total des faisceaux restants
    return sum(current.values())

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(7, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 7 | Part 2".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
