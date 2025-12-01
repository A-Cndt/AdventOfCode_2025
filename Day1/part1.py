#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 1
Part : 1

Ce script calcule le "password" pour l'énigme du jour 1, partie 1, 
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
    with open(f"./Day{day}/{file}", 'r') as f:
        return f.readlines()     
    
# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data) -> int:
    """
    Calcule le "password" en simulant les déplacements sur le module circulaire.

    La logique de la partie 1 incrémente le password à chaque passage exact sur 0.

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

        # Mise à jour de la position
        current_pos += movements

        # Position modulo MOD
        current_pos %= MOD

        # Incrément du password si passage exact sur 0
        if current_pos == 0:
            password += 1
            
    return password

# ===========================================================================

# %%
if __name__ == "__main__":
    result = solve(get_input(1, False))
    
    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 1 | Part 1".center(60))
    print("═" * 60)
    print(f"Password trouvé : \033[96m{result}\033[0m")
    print("═" * 60 + "\n")
