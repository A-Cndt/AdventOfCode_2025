#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 8
Part : 2

Ce script poursuit la logique de la Part 1 mais cette fois :
------------------------------------------------------------
On connecte les points dans l’ordre des distances croissantes,
comme dans Kruskal, jusqu'à ce que le graphe devienne entièrement
connecté (une seule composante).

L'arête qui réalise la connexion finale est la plus éloignée
dans l'arbre couvrant minimal.

Le résultat demandé est :
    produit des abscisses (x) des deux points reliés par cette
    dernière arête.

Concept :
----------
- calcul de toutes les distances au carré,
- tri des arêtes,
- union-find pour fusionner les composantes,
- quand il ne reste plus qu’une composante,
  on retourne x_i * x_j pour cette arête.

La logique est identique à ton implémentation originale,
seule la documentation est améliorée.

.. codeauthor:: Alexandre Condette <alexandre.condette@wanadoo.fr>
"""

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

# ===========================================================================
# Structures et fonctions utilitaires
class UnionFind:
    """
    Structure Union-Find (Disjoint Set Union).
    Fonctionne avec :
        - compression de chemin,
        - union par taille,
        - fusion des composantes.
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        """Retourne le représentant de la composante contenant x."""
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        """
        Fusionne les composantes de a et b.
        Retourne True si une fusion a eu lieu.
        """
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

# ---------------------------------------------------------------------------
def parse_coords(lines: list) -> list:
    """
    Convertit des lignes "x,y,z" en tuples (x, y, z).

    :param lines: lignes de texte
    :return: liste de tuples
    """
    pts = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        x, y, z = s.split(",")
        pts.append((int(x), int(y), int(z)))
    return pts


# ===========================================================================
# Résolution
def solve(lines: list) -> int:
    """
    Partie 2 : connexion complète du graphe.

    On :
    - génère toutes les arêtes avec distance,
    - trie les arêtes,
    - applique Kruskal,
    - quand il reste une seule composante,
      on retourne le produit des abscisses des deux points
      connectés par la dernière arête.

    :param lines: input brut
    :return: produit x_i * x_j de la dernière connexion
    """

    pts = parse_coords(lines)
    n = len(pts)

    if n <= 1:
        return 0

    # Construction de toutes les arêtes (dist², i, j)
    edges = []
    for i in range(n):
        xi, yi, zi = pts[i]
        for j in range(i + 1, n):
            xj, yj, zj = pts[j]
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            dist2 = dx * dx + dy * dy + dz * dz
            edges.append((dist2, i, j))

    # tri des arêtes par distance croissante
    edges.sort(key=lambda e: e[0])

    uf = UnionFind(n)
    components = n

    # Kruskal : on fusionne jusqu'à une seule composante
    for dist2, i, j in edges:
        if uf.union(i, j):
            components -= 1

            # dernière arête → graphe connecté
            if components == 1:
                x1 = pts[i][0]
                x2 = pts[j][0]
                return x1 * x2

    return 0

# ===========================================================================
if __name__ == "__main__":
    RESULT = solve(get_input(8, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 8 | Part 2".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")
