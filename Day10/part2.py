#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 10
Part : 2

Résolution ILP (Integer Linear Programming) full silencieuse
pour déterminer le nombre minimal d'appuis nécessaires afin
de configurer les compteurs de tension (« joltage »).

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Import
import os
import sys
from contextlib import contextmanager
from typing import List, Tuple

from pulp import (
    LpProblem, LpVariable, lpSum, LpMinimize, LpInteger,
    LpStatusOptimal, PULP_CBC_CMD
)

# ===========================================================================

# %% ========================================================================
# Lecture de l’input
def get_input(day: int = 1, example: bool = False) -> List[str]:
    """
    Lit le fichier d'entrée pour le jour demandé.

    :param day: Numéro du jour AoC
    :param example: True → example.txt, False → input.txt
    :return: Liste des lignes sans retour chariot
    """
    file = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{file}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]

# ===========================================================================

# %% ========================================================================
# Outils
@contextmanager
def suppress_output():
    """
    Contexte supprimant TOUTE sortie stdout/stderr durant son exécution.

    Utile pour neutraliser complètement les sorties verboses de CBC
    ou GLPK, même celles envoyées directement au terminal.
    """
    with open(os.devnull, 'w') as devnull:
        old_stdout, old_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = devnull, devnull
        try:
            yield
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr


# ---------------------------------------------------------------------------
def min_presses_joltage(target_list: List[int],
                        buttons: List[Tuple[int, ...]]) -> int:
    """
    Calcule exactement le nombre minimal d'appuis pour atteindre les
    compteurs de tension souhaités.

    Chaque bouton incrémente certains compteurs, et les variables de
    décision sont le nombre entier d'appuis par bouton.

    Modélisation ILP :
        - Variables : x_i ≥ 0 entiers (nb d'appuis du bouton i)
        - Contraintes : somme(x_i pour i affectant k) = target[k]
        - Objectif : min(sum(x_i))

    L'utilisation du solveur CBC est forcée et toute sortie est
    totalement supprimée.

    :param target_list: Liste des valeurs finales souhaitées par compteur
    :param buttons: Liste de boutons, chacun étant un tuple d'indices
                    de compteurs à incrémenter.
    :return: Nombre minimal d'appuis (int)
    """
    b = target_list
    n = len(b)
    m = len(buttons)

    if n == 0:
        return 0

    # Modèle
    prob = LpProblem("aoc_day10_part2", LpMinimize)

    # Variables : nombre d'appuis par bouton
    x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(m)]

    # Objectif : minimiser la somme des appuis
    prob += lpSum(x)

    # Contraintes : chaque compteur doit atteindre sa cible
    for k in range(n):
        prob += lpSum(x[i] for i, btn in enumerate(buttons) if k in btn) == b[k]

    # Solveur CBC silencieux
    solver = PULP_CBC_CMD(msg=False, keepFiles=False)

    with suppress_output():
        status = prob.solve(solver)

    if status != LpStatusOptimal:
        return None

    return int(sum(v.value() for v in x))

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(lines: List[str]) -> int:
    """
    Parse une ligne du type :

        [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}

    Extraction :
        - le schéma lumineux [] est ignoré
        - les boutons (a,b,c)
        - la cible {x,y,z}

    On calcule pour chaque machine le minimal d'appuis et on cumule.

    :param lines: Liste des lignes du fichier d'entrée
    :return: Somme des minima d'appuis pour toutes les machines
    """
    total = 0

    for line in lines:
        if not line.strip():
            continue

        # Ignorer la partie entre []
        after = line.split(']')[1] if ']' in line else line

        # ---- Boutons ----
        before_brace = after.split('{')[0].strip()
        parts = before_brace.split(')')

        buttons = []
        for p in parts:
            if '(' not in p:
                continue
            inside = p.split('(')[1].strip()
            if inside == '':
                buttons.append(())
            else:
                buttons.append(tuple(int(x) for x in inside.split(',') if x != ''))

        # ---- Cibles ----
        if '{' in line and '}' in line:
            inside = line.split('{')[1].split('}')[0]
            target_list = [int(x) for x in inside.split(',') if x.strip() != '']
        else:
            target_list = []

        res = min_presses_joltage(target_list, buttons)
        if res is None:
            raise ValueError(f"Aucune solution trouvée pour la ligne : {line!r}")

        total += res

    return total

# ===========================================================================

# %% ========================================================================
# MAIN
if __name__ == "__main__":
    RESULT = solve(get_input(10, False))   # True pour example, False pour input réel

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 10 | Part 2".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")

# ===========================================================================
