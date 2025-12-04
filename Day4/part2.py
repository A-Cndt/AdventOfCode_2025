#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 4
Part : 2

Ce script simule la suppression progressive des rouleaux de papier ("@") :
- Un rouleau est considéré accessible si moins de 4 voisins (sur 8 possibles)
  sont également des rouleaux.
- Tous les rouleaux accessibles peuvent être retirés simultanément.
- Leur retrait peut rendre accessibles d'autres rouleaux.
- Le processus se poursuit jusqu'à ce qu'aucun nouveau rouleau ne puisse être retiré.

Le résultat final correspond au nombre total de rouleaux retirés.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Imports

# ===========================================================================

# %% =
# Constantes
NEIGHBORS: list = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0), (1, 1)
]
# ==
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
    Simule les suppressions successives des rouleaux accessibles (<4 voisins)
    jusqu'à stabilisation.

    :param data: Liste brute des lignes d’input.
    :return: Nombre total de rouleaux retirés.
    :rtype: int
    """
    # --- Construction de l'ensemble des rouleaux "@"
    paper_rolls = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == "@":
                paper_rolls.add((y, x))

    total_removed = 0

    while True:
        to_remove = set()

        # Identifier les rouleaux accessibles (moins de 4 voisins)
        for (y, x) in paper_rolls:
            neighbor_count = 0
            for dy, dx in NEIGHBORS:
                neighbor = (y + dy, x + dx)
                if neighbor in paper_rolls:
                    neighbor_count += 1
            if neighbor_count < 4:
                to_remove.add((y, x))

        # Plus rien à retirer ? On a atteint la stabilité
        if not to_remove:
            break

        # Retirer tous les rouleaux accessibles en un tour
        paper_rolls -= to_remove
        total_removed += len(to_remove)

    return total_removed

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(4, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 4 | Part 2".center(60))
    print("═" * 60)
    print(f"Rouleaux retirés : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
