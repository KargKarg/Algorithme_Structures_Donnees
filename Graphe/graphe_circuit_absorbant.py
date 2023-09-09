from Graphe import graphe_lecture
from Structures import file
from File import file_ajouter, file_supprimer, file_vide
import numpy as np


def ford_bellman(path: str) -> bool:
    """
    Algorithme de Ford-Bellman pour détecter les circuits absorbants.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.

    Return:
        - (bool): Vrai si il y a un circuit absorbant, Faux sinon.
    """
    _, G_P, _, _ = graphe_lecture.matrice_adjacence(path, True, True)

    q = file.File(G_P.shape[0])

    pere = [None for _ in range(G_P.shape[0])]
    distance = [np.inf for _ in range(G_P.shape[0])]

    distance[0] = 0

    file_ajouter.ajouter(q, 1)

    cpt = 0

    while not file_vide.vide(q) and cpt < G_P.shape[0]**2:

        cpt += 1

        somm_act = file_supprimer.supprimer(q)
        dist_act = distance[somm_act-1]

        for j in range(G_P.shape[1]):
            if distance[j] > G_P[somm_act-1, j] + dist_act:
                distance[j] = G_P[somm_act-1, j] + dist_act
                pere[j] = somm_act
                file_ajouter.ajouter(q, j+1)

    if cpt < G_P.shape[0]**2:
        return False
    else:
        return True
