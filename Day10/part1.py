#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 10
Part : 1

Résolution du problème sous GF(2) : identification du nombre minimal
d'appuis de boutons permettant de reproduire un motif binaire ciblé.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# LECTURE DE L’INPUT
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée associé au jour demandé.

    :param day: Numéro du jour AoC.
    :param example: True → example.txt, False → input.txt.
    :return: Liste de chaînes, chaque ligne du fichier sans retour à la ligne.
    """
    file = "example.txt" if example else "input.txt"
    with open(f"./Day{day}/{file}", "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

# ===========================================================================

# %% ========================================================================
#  Fonctions utiles
def gauss(A: list, b: list):
    """
    Réduction de Gauss en arithmétique mod 2.

    :param A: Matrice binaire n×m (liste de listes).
    :param b: Vecteur binaire de taille n.
    :return:
        - is_ok : bool — une solution existe ?
        - x0 : solution particulière (liste binaire)
        - null_basis : base du noyau (liste de vecteurs binaires)
    """
    n = len(A)
    m = len(A[0]) if n > 0 else 0

    M = [row[:] + [rhs] for row, rhs in zip(A, b)]
    row = 0
    pivots = []

    # Pivotisation sur chaque colonne
    for col in range(m):
        sel = None
        for r in range(row, n):
            if M[r][col] == 1:
                sel = r
                break

        if sel is None:
            continue

        # Échange de lignes
        M[row], M[sel] = M[sel], M[row]
        pivots.append((row, col))

        # Élimination
        for r in range(n):
            if r != row and M[r][col] == 1:
                for c in range(col, m + 1):
                    M[r][c] ^= M[row][c]

        row += 1
        if row == n:
            break

    # Détection d'incohérence
    for r in range(row, n):
        if all(M[r][c] == 0 for c in range(m)) and M[r][m] == 1:
            return (False, None, None)

    # Solution particulière
    x0 = [0] * m
    for r, c in reversed(pivots):
        acc = M[r][m]
        for cc in range(c + 1, m):
            acc ^= (M[r][cc] & x0[cc])
        x0[c] = acc

    # Base du noyau
    pivot_cols = {c for _, c in pivots}
    free_cols = [c for c in range(m) if c not in pivot_cols]
    null_basis = []

    for f in free_cols:
        v = [0] * m
        v[f] = 1
        for r, c in reversed(pivots):
            s = 0
            for cc in range(c + 1, m):
                s ^= (M[r][cc] & v[cc])
            v[c] = s
        null_basis.append(v)

    return (True, x0, null_basis)

# ---------------------------------------------------------------------------
def weight(vec: list) -> int:
    """
    Calcule le poids de Hamming d’un vecteur binaire.

    Le poids correspond au nombre total de bits égaux à 1.  
    Utilisé pour mesurer le nombre d'appuis (ou la "taille") d'une solution
    dans l’espace GF(2).

    :param vec: Liste d'entiers 0/1.
    :return: Nombre d’éléments valant 1.
    """
    return sum(vec)

# ---------------------------------------------------------------------------
def add_mod2(u: list, v: list) -> list:
    """
    Effectue une addition binaire terme à terme (XOR).

    Cette opération correspond à l'addition dans le corps GF(2) :
    0⊕0=0, 1⊕0=1, 0⊕1=1, 1⊕1=0.  
    Employé pour combiner une solution particulière et des vecteurs du noyau.

    :param u: Premier vecteur binaire (liste 0/1).
    :param v: Second vecteur binaire (liste 0/1), même taille que u.
    :return: Nouveau vecteur résultant de u ⊕ v.
    """
    return [(a ^ b) for a, b in zip(u, v)]

# ---------------------------------------------------------------------------
def min_presses(target_str: str, buttons: list) -> int:
    """
    Calcule le nombre minimal d'appuis nécessaires pour reproduire
    un pattern binaire donné.

    :param target_str: Motif cible ('.' ou '#').
    :param buttons: Liste de tuples ; chaque bouton liste les positions togglées.
    :return: Nombre minimal d'appuis ou None si impossible.
    """
    n = len(target_str)
    b = [1 if c == "#" else 0 for c in target_str]
    m = len(buttons)

    # Construction de A (n × m)
    A = [[0] * m for _ in range(n)]
    for j, btn in enumerate(buttons):
        for idx in btn:
            A[idx][j] = 1

    ok, x0, null_basis = gauss(A, b)
    if not ok:
        return None

    k = len(null_basis)
    best = None

    # Cas dimension faible → exploration exhaustive
    if k <= 24:
        for mask in range(1 << k):
            x = x0[:]
            for i in range(k):
                if (mask >> i) & 1:
                    x = add_mod2(x, null_basis[i])
            w = weight(x)
            if best is None or w < best:
                best = w

    # Bruteforce direct si peu de boutons
    elif m <= 24:
        for mask in range(1 << m):
            state = [0] * n
            presses = 0
            for j in range(m):
                if (mask >> j) & 1:
                    presses += 1
                    for idx in buttons[j]:
                        state[idx] ^= 1
            if state == b and (best is None or presses < best):
                best = presses

    # Heuristique sinon
    else:
        x = x0[:]
        improved = True
        while improved:
            improved = False
            for v in null_basis:
                cand = add_mod2(x, v)
                if weight(cand) < weight(x):
                    x = cand
                    improved = True
        best = weight(x)

    return best

# ===========================================================================

# %% ========================================================================
# Résolution
def solve(lines: list) -> int:
    """
    Parse chaque ligne du fichier d'entrée puis applique la résolution GF(2).

    Format attendu :
        [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1)

    :param lines: Liste de lignes du fichier d'entrée.
    :return: Somme des minima pour toutes les lignes.
    """
    total = 0

    for line in lines:
        if not line.strip():
            continue

        diag = line.split("]")[0].split("[")[1]

        parts = line.split("]")[1].strip().split(")")
        buttons = []
        for p in parts:
            if "(" not in p:
                continue
            inside = p.split("(")[1]
            if inside.strip() == "":
                buttons.append(())
            else:
                buttons.append(tuple(int(x) for x in inside.split(",") if x != ""))

        res = min_presses(diag, buttons)
        total += res

    return total

# ===========================================================================

# %% ========================================================================
# MAIN
if __name__ == "__main__":
    RESULT = solve(get_input(10, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 10 | Part 1".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")

# ===========================================================================