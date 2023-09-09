from Graphe import graphe_lecture
import numpy as np


def dijkstra(path: str, origine: int) -> tuple:
    """
    Algorithme de Dijkstra pour le plus court chemin sur un graphe orienté.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.
        - origine (int): Sommet qui deviendra la racine de l'arborescence du PCC.

    Return:
        - pere (list): L'arborescence de PCC.
        - distance (list): Les distances de chaque sommet.
        - nb (list): Le nombre de PCC par sommet.
    """
    _, G_P, V, _ = graphe_lecture.matrice_adjacence(path, True, True)

    pere = [None for _ in range(G_P.shape[0])]
    distance = [np.inf for _ in range(G_P.shape[0])]
    nb = [0 for _ in range(G_P.shape[0])]

    distance[origine-1], nb[origine-1] = 0, 1

    traite = set().union({origine})

    for j in range(G_P.shape[1]):
        if distance[j] > G_P[origine-1, j]:
            distance[j] = G_P[origine-1, j]
            pere[j] = origine
            nb[j] = nb[origine-1]

    while traite != V:

        somm_act, distance_act = min((sommet, distance[sommet-1]) for sommet in (V-traite))

        traite.add(somm_act)

        for j in range(G_P.shape[1]):
            if distance[j] > G_P[somm_act-1, j] + distance_act:
                distance[j] = G_P[somm_act-1, j] + distance_act
                pere[j] = somm_act
                nb[j] = nb[somm_act-1]
            elif distance[j] == G_P[somm_act-1, j] + distance_act:
                nb[j] += nb[somm_act-1]

    return pere, distance, nb
