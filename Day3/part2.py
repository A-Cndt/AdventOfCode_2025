#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 3
Part : 2

Ce script extrait, pour chaque identifiant numérique, la plus grande
sous-séquence possible de longueur fixée tout en respectant l’ordre
d’apparition des chiffres.

L’objectif est d’optimiser la valeur numérique obtenue en conservant
exactement `n` digits parmi ceux présents dans l’identifiant d’origine.

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
def max_subsequence_as_number(digits: list, n: int) -> int:
    """
    Détermine la plus grande sous-séquence possible de longueur `n`
    en conservant l’ordre d’apparition des digits.

    On utilise ici une approche de type « monotonic stack » :
    - On sait combien de digits on peut supprimer : `m - n`
    - On construit une pile où chaque nouveau digit pousse les précédents
      plus petits, tant qu’on peut encore en retirer.
    - Le résultat final est simplement les `n` premiers digits de la pile.

    :param digits: liste de chiffres extraits de la ligne
    :param n: longueur de la sous-séquence maximale à conserver
    :return: le nombre entier formé par la sous-séquence maximale
    :rtype: int
    """
    m = len(digits)

    # Nombre total de suppressions possibles pour atteindre n digits
    remove = m - n 
    stack = []
    for d in digits:
        # Tant qu'on peut supprimer, et que le digit précédent est plus petit,
        # on le retire pour laisser place à un chiffre plus grand.
        while stack and remove > 0 and stack[-1] < d:
            stack.pop()
            remove -= 1
            
        # On empile le digit courant dans la séquence
        stack.append(d)

    # S'il reste des suppressions non utilisées,
    # on coupe simplement la fin de la pile.
    final = stack[:n]
    
    # Construction du nombre final
    return int("".join(str(d) for d in final))

# ---------------------------------------------------------------------------
def solve(data: list, n: int = 12) -> int:
    """
    Calcule la somme des plus grandes sous-séquences pour chaque ligne d’input.

    Pour chaque ligne :
    - Nettoyage du texte
    - Conversion en liste de digits
    - Extraction de la meilleure sous-séquence possible (length = n)
    - Accumulation du total

    :param data: lignes du fichier d’entrée
    :param n: longueur des sous-séquences à conserver
    :return: somme des valeurs trouvées
    :rtype: int
    """
    joltage = 0
    for line in data:
        line = line.strip()
        digits = [int(d) for d in line]

        joltage += max_subsequence_as_number(digits, n)
        
    return joltage

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(3, False), 12)
    
    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 3 | Part 2".center(60))
    print("═" * 60)
    print(f"Joltage trouvé : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")

