#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Advent Of Code 2025
===================
Day : 11
Part : 2

Résolution du problème : compter le nombre total de chemins allant de 'svr' vers 'out'
tout en imposant que chaque chemin passe obligatoirement par *dac* ET *fft*.
Le graphe est dirigé, potentiellement très ramifié, et l'exploration naïve serait
explosive. On utilise donc une recherche en profondeur combinée à un mécanisme
de mémoïsation afin d'éviter toute recomputation inutile.

L'état de recherche inclut le nœud courant ainsi que deux indicateurs booléens
permettant de savoir si 'dac' et/ou 'fft' ont déjà été visités.
"""

# ===========================================================================

# %% ========================================================================
# LECTURE DE L’INPUT
def get_input(day: int = 1, example: bool = False) -> list:
    """
    Lit le fichier d'entrée associé au jour donné.

    :param day: Numéro du jour AoC.
    :param example: True → example.txt, False → input.txt.
    :return: Liste de lignes (chaînes de caractères) sans retour à la ligne final.
    """
    # /!\ Jour11 la part2 à son propre fichier d'exemple
    file = "example2.txt" if example else "input.txt"
    with open(f"./Day{day}/{file}", "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

# ===========================================================================


# %% ========================================================================
# Résolution
def solve(data: list) -> int:
    """
    Compte le nombre total de chemins allant de 'svr' à 'out' et passant
    obligatoirement par les nœuds 'dac' et 'fft'.

    Le graphe est décrit sous la forme :
        device: a b c
    signifiant que `device` pointe vers les nœuds a, b, c.

    La fonction réalise une exploration DFS annotée :
    - Chaque appel de dfs(device, seen_dac, seen_fft) représente un état unique
      associé au nœud courant et aux flags déjà rencontrés.
    - Un cache (memo) évite de recalculer les sous-chemins identiques.
    - Lorsqu'on atteint 'out', on ne valide le chemin que si DAC ET FFT ont
      effectivement été rencontrés.

    :param data: Liste de lignes représentant le graphe.
    :return: Nombre total de chemins valides.
    """
    # Construction du graphe sous forme de dictionnaire { noeud: [sorties...] }
    server = {}
    for line in data:
        device, outputs = line.split(": ")
        server[device] = outputs.split()

    # Mémoïsation :
    # (device, seen_dac, seen_fft) → nombre de chemins valides depuis cet état.
    memo = {}

    def dfs(device: str, seen_dac: bool, seen_fft: bool) -> int:
        """
        Explore récursivement tous les chemins depuis 'device'.
        Les indicateurs seen_dac et seen_fft suivent l'état du chemin courant.
        """
        key = (device, seen_dac, seen_fft)

        # Résultat déjà calculé → accélération massive sur les grands graphes
        if key in memo:
            return memo[key]

        # Cas terminal : arrivée sur 'out'
        if device == "out":
            # Le chemin est valide uniquement si les deux nœuds obligatoires ont été vus
            memo[key] = 1 if (seen_dac and seen_fft) else 0
            return memo[key]

        total = 0

        # Exploration des successeurs
        for nxt in server.get(device, []):
            total += dfs(
                nxt,
                seen_dac or (nxt == "dac"),   # Mémoire de passage par 'dac'
                seen_fft or (nxt == "fft")    # Mémoire de passage par 'fft'
            )

        memo[key] = total
        return total

    # Lancement depuis la racine
    return dfs("svr", False, False)

# ===========================================================================


# %% ========================================================================
# MAIN
if __name__ == "__main__":
    RESULT = solve(get_input(11, False))

    print("\n" + "═" * 60)
    print("   🔐 Advent of Code 2025 — Day 11 | Part 2".center(60))
    print("═" * 60)
    print(f"Résultat : \033[96m{RESULT}\033[0m")
    print("═" * 60 + "\n")

# ===========================================================================
