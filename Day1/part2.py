#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 1
Part : 2

Ce script calcule le "password" pour l'énigme du jour 1, partie 2, 
en suivant la logique de déplacements circulaires sur un module MOD.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Constantes
MOD: int = 100                     # Taille du module (0..99)
SIGNS: dict = {"R": 1, "L": -1}    # Mapping direction → signe

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
        return f.readlines()

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data) -> int:
    """
    Calcule le "password" en simulant les déplacements sur le module circulaire.

    La logique de calcul de la partie 2 inclut la correction des passages exacts sur 0
    avec des mouvements négatifs.

    :param data: liste de mouvements sous forme de chaînes, ex. "R10", "L5"
    :return: valeur finale du password
    :rtype: int
    """
    password: int       = 0      # compteur de passages "modulo" sur 0
    current_pos: int    = 50     # position initiale

    for line in data:
        line = line.strip()  # nettoyage

        # Calcul du mouvement signé (dépend de la direction)
        movements: int = int(line[1:]) * SIGNS[line[0]]

        # Position non modulo après le mouvement
        next_pos = current_pos + movements

        # Nombre de passages "modulo" entre current_pos et next_pos
        div = next_pos // MOD - current_pos // MOD

        # Mise à jour du password avec correction des passages sur 0
        password += abs(div) \
                    - int(current_pos == 0 and div < 0) \
                    + int(next_pos % MOD == 0 and movements < 0)

        # Nouvelle position modulo
        current_pos = next_pos % MOD

    return password

# ===========================================================================

# %%
if __name__ == "__main__":
    result = solve(get_input(1, False))
    
    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 1 | Part 2".center(60))
    print("═" * 60)
    print(f"Password (méthode 0x434C49434B) : \033[96m{result}\033[0m")
    print("═" * 60 + "\n")
