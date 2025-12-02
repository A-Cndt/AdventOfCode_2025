#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 2
Part : 1

Ce script identifie tous les identifiants "invalides" dans une liste 
de plages numériques. Un ID est invalide s'il est composé de deux fois 
la même séquence de chiffres (ex : 12  → 1212,  345 → 345345).

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Imports
from math import ceil, floor
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
        return f.read()

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data: list) -> int:
    """
    Calcule la somme de tous les identifiants invalides dans les plages spécifiées.

    Une plage a la forme "A-B". Un ID est considéré invalide si sa
    représentation est constituée de *deux fois* la même séquence de chiffres :
        - 11   → invalide (1 répété deux fois)
        - 1212 → invalide (12 répété deux fois)
        - 9999 → invalide (99 répété deux fois)
        - etc.

    Optimisation :
        - Plutôt que de tester chaque nombre : on détecte mathématiquement
          toutes les valeurs ayant le pattern s * m où m = 10^k + 1.

    :param data: Chaîne contenant plusieurs plages, séparées par des virgules.
    :return: Somme de tous les identifiants invalides présents dans les plages.
    :rtype: int
    """
    invalid_id: int = 0
    all_ids = data.split(",")
    
    for ids in all_ids:
        # Extraction bornes [start, stop]
        start, stop = ids.split('-')
        start = int(start)
        stop = int(stop) + 1 # inclure la borne supérieure
        
        # Kmax = nombre max de digits pour les patterns divisés en deux (ex: 1234 → k=2)
        Kmax = floor(len(str(stop)) / 2)

        for k in range(1, Kmax + 1):
            # m = 10^k + 1 → génère les nombres duplicables (ex : k=2 → 101 → s  * 101 = ss)
            m = 10 ** k + 1
            
            # On cherche les valeurs s telles que s*m tombe dans [start, stop]
            s_lo = ceil(start / m)
            s_hi = floor(stop / m)
            
            # Restreindre s aux nombres k-digits
            s_lo = max(s_lo, 10 ** (k - 1))
            s_hi = min(s_hi, 10 ** k - 1)
            
            # Si la borne basse dépasse la borne haute → aucune valeur possible
            if s_lo <= s_hi:
                # Nombre de valeurs possibles
                count = s_hi - s_lo + 1
                # Somme des s du range
                sum_s = (s_lo + s_hi) * count // 2
                # Contribution total = m * somme(s)
                invalid_id += m * sum_s
                    
    return invalid_id

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(2, False))
    
    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 2 | Part 1".center(60))
    print("═" * 60)
    print(f"ID Invalides trouvés : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
