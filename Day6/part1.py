#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 6
Part : 1

Ce script résout le puzzle Day 6 en évaluant une série d’expressions 
mathématiques disposées en colonnes.

L’entrée possède deux sections :
    - Une première section contenant les valeurs (opérandes), une valeur par cellule
    - Une dernière ligne contenant les opérateurs à appliquer entre les colonnes

Chaque colonne représente une expression à évaluer :
    operand_0 <op> operand_1 <op> operand_2 <op> ...

Les expressions sont évaluées de gauche à droite conformément aux opérateurs fournis.
La somme des résultats de toutes les colonnes constitue la sortie finale.

La logique générale :
    1. Nettoyage et restructuration des lignes pour obtenir une matrice opérandes × colonnes
    2. Extraction des opérateurs (dernière ligne)
    3. Construction des expressions colonne par colonne
    4. Évaluation des expressions
    5. Addition des résultats

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""


# %% ========================================================================
# Lecture de l'entrée
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée pour le jour donné.

    :param day: Numéro du jour AOC (ex : 6 pour Day 6)
    :param example: Si True → example.txt, sinon → input.txt
    :return: Liste des lignes brutes du fichier
    """
    filename = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{filename}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


# ===========================================================================

# %% ========================================================================
# Résolution
def solve(lines: list) -> int:
    """
    Évalue les expressions mathématiques colonne par colonne 
    et retourne la somme des résultats.

    Fonctionnement :
        - Toutes les lignes sauf la dernière contiennent les opérandes
        - La dernière ligne contient les opérateurs
        - Chaque colonne est transformée en une expression (string)
        - L'expression est évaluée via eval()
        - Le résultat est ajouté à une somme globale

    :param lines: List[str], lignes de l'entrée
    :return: Somme des résultats des expressions
    """
    total_sum = 0

    # --- Extraction des opérandes ---
    # On nettoie les espaces inutiles, on obtient une matrice : lignes × colonnes
    operands_matrix = []
    for line in lines[:-1]:
        cleaned = [token.strip() for token in line.split(' ') if token != '']
        operands_matrix.append(cleaned)

    # --- Extraction des opérateurs ---
    operators = [op.strip() for op in lines[-1].split(' ') if op != '']

    # --- Évaluation colonne par colonne ---
    nb_columns = len(operators)

    for col in range(nb_columns):
        expression = ""

        # Construction de l’expression : v0 op v1 op v2 ...
        for row in range(len(operands_matrix)):
            expression += operands_matrix[row][col]

            if row != len(operands_matrix) - 1:
                expression += operators[col]

        # Évaluation de la colonne et accumulation
        total_sum += eval(expression)

    return total_sum


# ===========================================================================

# %%
if __name__ == "__main__":
    RESULT = solve(get_input(6, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 6 | Part 1".center(60))
    print("═" * 60)
    print(f"Grand Total : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
