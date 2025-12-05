#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 5
Part : 2

Ce script calcule le nombre total d'identifiants présents dans l'ensemble 
des intervalles définis dans la première section de l'input.

Chaque intervalle est défini sous la forme "start-stop". La solution ne 
génère pas tous les identifiants individuellement ; elle fusionne les 
intervalles qui se chevauchent ou sont contigus, puis calcule la somme 
des longueurs des intervalles fusionnés pour obtenir le résultat final.

Cette approche permet de gérer efficacement un très grand nombre de valeurs 
sans explosion mémoire.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""


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
     Calcule le nombre total d'identifiants inclus dans les intervalles.

    L'input est supposé structuré avec :
    - Une première section contenant des intervalles "start-stop".
    - Une section suivante contenant éventuellement d'autres informations
      ou identifiants, qui sont ignorés dans cette partie.

    Étapes principales :
    1. Extraction de tous les intervalles.
    2. Tri des intervalles par début.
    3. Fusion des intervalles qui se chevauchent ou sont contigus.
    4. Somme des longueurs des intervalles fusionnés pour obtenir le total.

    :param data: Liste brute des lignes du fichier.
    :return: Nombre total d'identifiants présents dans les intervalles.
    :rtype: int
    """
    intervals: list = []

    # 1. Collecte uniquement les intervalles
    for line in data:
        if "-" in line:
            start, stop = map(int, line.split("-"))
            intervals.append((start, stop))
        else:
            continue # On arrête à la fin de la section des intervalles

    # 2. Tri des intervalles
    intervals.sort()

    # 3. Fusion des intervalles
    merged = []
    for start, stop in intervals:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, stop])
        else:
            merged[-1][1] = max(merged[-1][1], stop)

    # 4. Calcul du nombre total d'identifiants
    fresh = sum(stop - start + 1 for start, stop in merged)

    return fresh

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(5, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 5 | Part 2".center(60))
    print("═" * 60)
    print(f"Ingrédients frais : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
