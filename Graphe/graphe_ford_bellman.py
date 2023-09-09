from Graphe import graphe_lecture
import numpy as np
from Structures import file
from File import file_ajouter, file_supprimer, file_vide


def ford_bellman(path: str, origine: int) -> tuple:
    """
    Algorithme de Ford-Bellman pour le plus court chemin sur un graphe orienté.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.
        - origine (int): Sommet qui deviendra la racine de l'arborescence du PCC.

    Return:
        - pere (list): L'arborescence de PCC.
        - distance (list): Les distances de chaque sommet.
    """
    _, G_P, _, _ = graphe_lecture.matrice_adjacence(path, True, True)

    q = file.File(G_P.shape[0])

    pere = [None for _ in range(G_P.shape[0])]
    distance = [np.inf for _ in range(G_P.shape[0])]

    distance[origine-1] = 0

    file_ajouter.ajouter(q, origine)

    while not file_vide.vide(q):

        somm_act = file_supprimer.supprimer(q)
        dist_act = distance[somm_act-1]

        for j in range(G_P.shape[1]):
            if distance[j] > G_P[somm_act-1, j] + dist_act:
                distance[j] = G_P[somm_act-1, j] + dist_act
                pere[j] = somm_act
                file_ajouter.ajouter(q, j+1)

    return pere, distance
