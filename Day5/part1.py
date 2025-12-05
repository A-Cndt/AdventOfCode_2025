#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 5
Part : 1

Ce script calcule combien d'identifiants apparaissant dans la seconde partie de 
l'input appartiennent à l'un des intervalles définis dans la première partie.

Chaque intervalle est défini sous la forme "start-stop". Les lignes suivantes 
peuvent contenir des identifiants individuels. Un identifiant est comptabilisé 
dès qu'il appartient à au moins un intervalle présent dans la liste.

La logique se base sur :
- l'extraction de tous les intervalles "start-stop",
- la vérification de chaque identifiant individuel pour déterminer s'il est
  inclus dans l'un des intervalles collectés.

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
     Analyse les lignes d'input et calcule le nombre d'identifiants individuels 
    présents dans l'un des intervalles définis plus haut dans le fichier.

    L'input est supposé structuré comme suit :
    - Première section : plusieurs lignes au format "start-stop".
    - Deuxième section : des identifiants uniques, un par ligne.

    Pour chaque identifiant rencontré, le script vérifie s'il appartient à 
    l'une des plages collectées. Dès qu'un intervalle contient l'ID, il est 
    comptabilisé et la recherche pour cet ID s'arrête.

    :param data: Liste brute des lignes du fichier.
    :return: Nombre d'identifiants appartenant à au moins un intervalle.
    :rtype: int
    """
    fresh: int = 0
    intervals: list = []

    # 1. Collecte des intervalles
    for line in data:
        if "-" in line:
            start, stop = map(int, line.split("-"))
            intervals.append((start, stop))

    # 2. Vérification des IDs uniques
    for line in data:
        if "-" not in line and line:
            id = int(line)
            
            # Test d'appartenance à l'un des intervalles
            for start, stop in intervals:
                if start <= id <= stop:
                    fresh += 1
                    break

    return fresh

# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(5, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 5 | Part 1".center(60))
    print("═" * 60)
    print(f"Ingrédients frais : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
