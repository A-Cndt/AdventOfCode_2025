#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 3
Part : 1

Ce script identifie les deux digits à conserver dans chaque ligne afin de 
former le plus grand nombre possible selon la logique originale de la Part 1 :
- On identifie le plus grand digit (sauf le dernier),
- Puis on cherche le plus grand digit restant après l'index de celui-ci,
- Le joltage est la concaténation de ces deux chiffres.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Imports

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
def solve(data: list) -> int:
    """
    Calcule le joltage total de toutes les lignes selon la règle de la Part 1 :
    
    Pour chaque ligne :
    -------------------
    - On convertit chaque caractère en digit.
    - On cherche le plus grand digit parmi tous sauf le dernier.
    - On récupère son index.
    - À partir de ce point, on cherche le plus grand digit restant.
    - On concatène les deux digits trouvés.
    - On ajoute cette valeur au joltage total.

    :param data: Liste brute des lignes d’input.
    :return: Joltage total.
    :rtype: int
    """
    joltage: int = 0
    
    for line in data:
        # Nettoie la ligne (retire \n, espaces)
        line = line.strip()
        
        # Convertit la ligne en liste de digits
        digits = [int(d) for d in line]
        
        # Premier digit : le maximum dans tous les digits SAUF le dernier
        first_digit = str(max(digits[:-1]))
        
        # Position du premier digit dans la liste, puis on avance d'un cran
        index = digits.index(int(first_digit)) + 1
        
         # Second digit : le maximum dans la partie restante à droite
        second_digit = str(max(digits[index:]))
        
        # Ajout au cumul du joltage
        joltage += int(first_digit + second_digit)
        
    return joltage

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(3, False))
    
    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 3 | Part 1".center(60))
    print("═" * 60)
    print(f"Joltage trouvé : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")

