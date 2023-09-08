from Graphe import graphe_lecture
from Graphe import graphe_cycle
import numpy as np


def kruskall(path: str) -> tuple:
    """
    Algorithme de Kruskall pour le calcul du sous arbre couvrant de poids minimum.

    Argument:
        - path (str): Chemin vers le graphe au format texte.

    Return:
        - arbre (numpy.array): La matrice d'adjacence de l'arbre.
        - aretes_arbre (set): Les arêtes de l'arbre.
    """
    _, G_p, _, _ = graphe_lecture.matrice_adjacence(path, False, True)

    arbre = np.full(G_p.shape, 0)
    aretes_arbre = set()

    while len(aretes_arbre) != G_p.shape[0]-1:

        minimum, mi, mj = np.inf, 0, 0

        for i in range(G_p.shape[0]):
            for j in range(G_p.shape[1]):
                if i != j and (i+1, j+1) not in aretes_arbre and (j+1, i+1) not in aretes_arbre and G_p[i, j] < minimum:
                    arbre[i, j], arbre[j, i] = 1, 1
                    if graphe_cycle.cycle(arbre):
                        arbre[i, j], arbre[j, i] = 0, 0
                    else:
                        minimum, mi, mj = G_p[i, j], i, j
                        arbre[i, j], arbre[j, i] = 0, 0

        arbre[mi, mj], arbre[mj, mi] = 1, 1
        aretes_arbre.add((mi + 1, mj + 1))

    return arbre, aretes_arbre
