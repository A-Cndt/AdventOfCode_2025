#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 6
Part : 2

Dans cette partie, les chiffres des “problèmes” sont disposés en colonnes
(verticalement), tandis que les opérateurs (+ ou *) apparaissent sur la dernière ligne.

La lecture se fait **de droite à gauche** :
    - chaque colonne contenant des digits représente un nombre,
    - une colonne entièrement vide signifie que le nombre est terminé,
    - à ce moment, on applique l’opérateur correspondant,
    - puis on ajoute le résultat au total.

On répète ce procédé pour toutes les colonnes.

Le résultat final est la somme de tous les blocs évalués.

La logique est :
    1. uniformiser la largeur des lignes,
    2. parcourir les colonnes de droite à gauche,
    3. construire les nombres,
    4. déclencher les opérations sur les colonnes vides,
    5. accumuler les résultats.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""
# %% ========================================================================
# Imports
from math import prod
# ===========================================================================

# %% ========================================================================
# Input data
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée pour le jour donné.

    :param day: numéro du jour AoC
    :param example: True pour example.txt, False pour input.txt
    :return: liste des lignes du fichier
    """
    filename = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{filename}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


# ===========================================================================

# %% ========================================================================
# Résolution
def solve(data: list) -> int:
    """
    Résout la partie 2 : évaluation des problèmes lus verticalement.

    Chaque colonne (de droite à gauche) contient les chiffres d’un nombre.
    Une colonne vide déclenche l’évaluation du bloc de nombres collectés,
    à l’aide de l'opérateur correspondant dans la dernière ligne.

    :param data: lignes du fichier AoC
    :return: total des résultats des blocs
    """

    # Séparation : lignes contenant les chiffres et ligne des opérateurs
    digit_rows = [line.rstrip("\n") for line in data[:-1]]
    operator_row = data[-1].rstrip("\n")

    # Normalisation des largeurs pour lisibilité colonne par colonne
    width = max(len(row) for row in digit_rows + [operator_row])
    digit_rows = [row.ljust(width) for row in digit_rows]
    operator_row = operator_row.ljust(width)

    # Les opérateurs sont lus de droite à gauche → on les stocke dans une pile
    operators = [c for c in operator_row if c != " "]

    total = 0            # résultat final
    current_numbers = [] # nombres collectés dans le bloc courant

    # Parcours des colonnes droite → gauche
    for col in range(width - 1, -2, -1):

        # Cas déclencheur : colonne vide ou fin de parcours
        if col == -1 or all(row[col] == ' ' for row in digit_rows):

            # On applique l’opération sur le bloc collecté
            op = operators.pop()

            if op == '+':
                total += sum(current_numbers)
            elif op == '*':
                total += prod(current_numbers)
            else:
                raise ValueError(f"Opérateur inconnu : {op}")

            # On réinitialise pour le bloc suivant
            current_numbers = []

        else:
            # Construction du nombre vertical
            digits = ''.join(row[col] for row in digit_rows).strip()
            current_numbers.append(int(digits))

    return total


# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(6, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 6 | Part 2".center(60))
    print("═" * 60)
    print(f"Grand Total : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
