import numpy as np
from Graphe import graphe_lecture


def floyd_warshall(path: str):
    """
    Algorithme de Floyd-Warshall pour les PCC entre chaque couple de sommets.

    Complexité:
        - O(n^3)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.

    Return:
        - W (numpy.array): La matrice des poids.
            -> W[i, j] = Le PCC de i à j
        - matrice_successeurs (numpy.array): La matrice des successeurs des PCC.
            -> matrice_successeurs[i, j] = Le successeur de i sur le PCC de i à j.
    """
    _, G_P, _, _ = graphe_lecture.matrice_adjacence(path, True, True)

    W = G_P.copy()
    matrice_successeurs = np.empty(W.shape, dtype=object)

    for i in range(G_P.shape[0]):
        for j in range(G_P.shape[0]):
            if i != j and G_P[i, j] != np.inf:
                matrice_successeurs[i, j] = j+1

    for k in range(matrice_successeurs.shape[0]):
        matrice_successeurs[k, k] = k+1
        W[k, k] = 0
        for i in range(W.shape[0]):
            for j in range(W.shape[1]):
                if W[i, j] > W[i, k] + W[k, j]:
                    W[i, j] = W[i, k] + W[k, j]
                    matrice_successeurs[i, j] = matrice_successeurs[i, k]

    return W, matrice_successeurs
