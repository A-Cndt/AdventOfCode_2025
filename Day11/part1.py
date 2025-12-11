#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 11
Part : 1

Ce module implémente la résolution du problème du jour sous la forme d'une
exploration de graphe dirigé. Chaque ligne du fichier d'entrée décrit un
device et la liste des devices vers lesquels il envoie ses données.

L’objectif est de déterminer le nombre total de chemins distincts menant du
device d’entrée ("you") au device de sortie ("out").

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# LECTURE DE L’INPUT
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit et retourne le contenu du fichier d'entrée externe.

    Les fichiers sont stockés dans un dossier `DayX/` où X correspond
    au numéro du jour AoC. Deux fichiers peuvent exister :
    - example.txt : jeu de données simplifié fourni par l’énoncé
    - input.txt   : jeu de données complet pour la soumission AoC

    Parameters
    ----------
    day : int, optional
        Numéro du jour AoC. Par défaut 1.
    example : bool, optional
        Si True, lit `example.txt`. Si False, lit `input.txt`.

    Returns
    -------
    list of str
        Liste des lignes du fichier, sans retour chariot final.
    """
    file = "example.txt" if example else "input.txt"
    with open(f"./Day{day}/{file}", "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

# ===========================================================================


# %% ========================================================================
# RÉSOLUTION
def solve(data: list) -> int:
    """
    Calcule le nombre total de chemins menant du device 'you' au device 'out'.

    Le fichier d’entrée décrit un graphe dirigé où chaque device possède une
    liste d’outputs. À partir de ce graphe, une recherche en profondeur (DFS)
    est effectuée pour dénombrer tous les chemins distincts possibles.

    Format attendu pour chaque ligne :
        "aaa: bbb ccc ddd"

    où "aaa" est le device, et "bbb ccc ddd" les devices accessibles depuis lui.

    Parameters
    ----------
    data : list of str
        Liste des lignes brutes du fichier d’entrée.

    Returns
    -------
    int
        Nombre total de chemins distincts de 'you' vers 'out'.
    """
    # Construction du graphe : {device: [liste_outputs]}
    server = {}
    for line in data:
        device, outputs = line.split(": ")
        server[device] = outputs.split()

    # Compteur de chemins trouvés
    paths = 0

    def dfs(device: str) -> None:
        """
        Parcourt récursivement le graphe à partir d’un device.

        Si la fonction atteint 'out', un chemin complet a été trouvé.
        """
        nonlocal paths

        # Condition d'arrêt : device final
        if device == "out":
            paths += 1
            return

        # Exploration des sorties disponibles
        for nxt in server.get(device, []):
            dfs(nxt)

    # Device de départ imposé par l’énoncé
    dfs("you")

    return paths

# ===========================================================================


# %% ========================================================================
# MAIN
if __name__ == "__main__":
    RESULT = solve(get_input(11, True))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 11 | Part 1".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")

# ===========================================================================
