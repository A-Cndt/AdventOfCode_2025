#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 2
Part : 2

Ce script identifie et additionne tous les identifiants invalides dans
les intervalles fournis. Un identifiant est considéré invalide s'il est
entièrement composé d'un motif de chiffres répété au moins deux fois.

Exemples :
    - 12341234  → motif "1234" répété deux fois
    - 1111111   → motif "1" répété sept fois
    - 565656    → motif "56" répété trois fois

Cette version utilise une méthode directe et fiable pour vérifier
les motifs répétés.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Constantes
N: int = 2
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
def is_repeated_pattern(x: int, n: int = 2) -> bool:
    """
    Vérifie si un entier `x` est composé d'un motif répété au moins `n` fois.

    La logique :
        - Convertir le nombre en chaîne.
        - Tester toutes les longueurs possibles de motif (1 à L/n).
        - Un motif est valide si :
            * sa longueur divise exactement la longueur totale,
            * il se répète assez de fois (au moins `n`),
            * la concaténation du motif recrée le nombre.

    :param x: entier à analyser
    :param n: nombre minimal de répétitions requises
    :return: True si `x` est invalide (motif répété), False sinon
    :rtype: bool
    """
    L:str = len(str(x))
    
    for k in range(1, L // n + 1):
        if L % k != 0 :
            continue
        
        times = L // k
        if times < n :
            continue
        
        pattern = str(x)[:k]
        if pattern * times == str(x):
            return True
        
    return False

# ---------------------------------------------------------------------------
def solve(data: list, n: int = 2) -> int:
    """
    Parcourt chaque intervalle "start-stop" listé dans l'input
    et additionne tous les identifiants invalides selon la règle
    des motifs répétés.

    :param data: chaîne contenant les intervalles séparés par des virgules
    :param n: nombre minimal de répétitions exigées pour être invalide
    :return: somme de tous les identifiants invalides
    :rtype: int
    """
    invalid_id: int = 0
    all_ids = data.split(",")

    for ids in all_ids:
        start, stop = ids.split("-")
        start = int(start)
        stop = int(stop)
        
        # Vérification brute-force (fiable pour la taille de l'énigme)
        for x in range(start, stop + 1):
            if is_repeated_pattern(x, n):
                invalid_id += x
                    
    return invalid_id

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(2, False), N)
    
    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 2 | Part 2".center(60))
    print("═" * 60)
    print(f"ID Invalides trouvés : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
