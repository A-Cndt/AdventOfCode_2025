#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 8
Part : 1

Ce script identifie les trois plus grandes composantes connectées dans un nuage
de points 3D en utilisant seulement les 1000 arêtes les plus proches.

Concept :
----------
- Chaque point est un tuple (x, y, z).
- On calcule toutes les distances au carré entre les points.
- On garde uniquement les K plus petites distances (1000 par défaut).
- Chaque paire sélectionnée relie deux points dans une structure Union-Find.
- Une fois les unions réalisées, on récupère les tailles des composantes.
- Le résultat est le produit des tailles des trois plus grandes composantes.

L’objectif correspond exactement à l'énoncé AoC 2025 Day 8 Part 1.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

# %% ========================================================================
# Import
import heapq

# ===========================================================================

# %% ========================================================================
# Lecture de l’input
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée pour le jour demandé.

    :param day: numéro du jour AoC
    :param example: True → example.txt, False → input.txt
    :return: liste des lignes sans fin de ligne
    """
    filename = 'example.txt' if example else 'input.txt'
    with open(f"./Day{day}/{filename}", 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


# ===========================================================================

# %% ========================================================================
# Structures et fonctions utilitaires
class UnionFind:
    """
    Structure Union-Find (Disjoint Set Union) avec :
    - compression de chemin,
    - union par taille,
    - extraction des tailles de composantes.
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        """Retourne le représentant du set contenant x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        """
        Fusionne les ensembles contenant a et b.
        Retourne True si une fusion a réellement eu lieu.
        """
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        # union par taille
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

        return True

    def component_sizes(self):
        """Retourne les tailles des composantes, triées décroissantes."""
        roots = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            roots[r] = roots.get(r, 0) + 1
        return sorted(roots.values(), reverse=True)

# ---------------------------------------------------------------------------
def parse_coords(lines: list) -> list:
    """
    Convertit une liste de lignes au format "x,y,z" en tuples.

    Accepté :
    - lignes chaînes,
    - tuples déjà formés.

    :return: liste de tuples (x, y, z)
    """
    pts = []

    for line in lines:
        if isinstance(line, tuple):
            pts.append(line)
            continue

        s = line.strip()
        if not s:
            continue

        x, y, z = s.split(",")
        pts.append((int(x), int(y), int(z)))

    return pts

# ===========================================================================
# Résolution
def solve(lines, K=1000):
    """
    Résout la partie 1 :
    - calcule toutes les distances,
    - garde les K plus petites,
    - les fusionne dans un Union-Find,
    - produit les tailles des 3 plus grandes composantes.

    :param lines: lignes de points
    :param K: nombre de paires à conserver
    :return: produit des trois plus grandes composantes
    """
    pts = [tuple(map(int, l.split(","))) for l in lines if l.strip()]
    n = len(pts)

    # calcul brute des distances (comme dans ton code)
    pairs = []
    for i in range(n):
        xi, yi, zi = pts[i]
        for j in range(i + 1, n):
            xj, yj, zj = pts[j]
            d2 = (xi - xj)**2 + (yi - yj)**2 + (zi - zj)**2
            pairs.append((d2, i, j))

    # garde les K plus proches
    pairs = heapq.nsmallest(K, pairs, key=lambda x: x[0])

    uf = UnionFind(n)

    for _, i, j in pairs:
        uf.union(i, j)

    sizes = uf.component_sizes()
    return sizes[0] * sizes[1] * sizes[2]

# ===========================================================================
# %%
if __name__ == "__main__":
    RESULT = solve(get_input(8, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 8 | Part 1".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
