from Graphe import graphe_lecture
from Graphe import graphe_cycle
import numpy as np


def prim(path: str) -> tuple:
    """
    Algorithme de Prim pour le calcul du sous arbre couvrant de poids minimum.

    Argument:
        - path (str): Chemin vers le graphe au format texte.

    Return:
        - arbre (numpy.array): La matrice d'adjacence de l'arbre.
        - sommets_arbre (set): Les sommets de l'arbre
        - aretes_arbre (set): Les arêtes de l'arbre.
    """
    _, G_p, _, _ = graphe_lecture.matrice_adjacence(path, False, True)

    arbre = np.full(G_p.shape, 0)

    minimum, mi, mj = np.inf, 0, 0

    for i in range(G_p.shape[0]):
        for j in range(G_p.shape[1]):
            if i != j and G_p[i, j] < minimum:
                minimum, mi, mj = G_p[i, j], i, j

    sommets_arbre, aretes_arbre = set().union({mi+1, mj+1}), set()
    aretes_arbre.add((mi+1, mj+1))

    arbre[mi, mj], arbre[mj, mi] = 1, 1

    while len(aretes_arbre) != G_p.shape[0] - 1:

        minimum, mi, mj = np.inf, 0, 0

        for i in sommets_arbre:
            for j in range(G_p.shape[1]):
                if i-1 != j and (i, j+1) not in aretes_arbre and (j+1, i) not in aretes_arbre and G_p[i-1, j] < minimum:
                    arbre[i-1, j], arbre[j, i-1] = 1, 1
                    if graphe_cycle.cycle(arbre):
                        arbre[i-1, j], arbre[j, i-1] = 0, 0
                    else:
                        minimum, mi, mj = G_p[i-1, j], i-1, j
                        arbre[i-1, j], arbre[j, i-1] = 0, 0

        arbre[mi, mj], arbre[mj, mi] = 1, 1
        sommets_arbre = sommets_arbre.union({mi+1, mj+1})
        aretes_arbre.add((mi+1, mj+1))

    return arbre, sommets_arbre, aretes_arbre
