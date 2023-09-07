import numpy as np


def non_oriente(G):
    """
    Algorithme calculant la matrice d'adjacence non orienté d'un graphe orienté.

    Complexité:
        - O(n^2)

    Argument:
        - G (numpy.array): Matrice d'adjacence du graphe orienté.

    Retour:
        - G_no (numpy.array): Matrice d'adjacence non orienté.
    """
    G_no = np.full(G.shape, 0, int)

    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            if G[i, j] == 1:
                G_no[i, j] = 1
                G_no[j, i] = 1
    return G_no


def complementaire(G):
    """
    Algorithme calculant la matrice d'adjacence du graphe complémentaire.

    Complexité:
        - 0(n^2)

    Argument:
        - G (numpy.array): La matrice d'adjacence du graphe.

    Return:
        - G_comp (numpy.array): La matrice d'adjacence du graphe complémentaire.
    """
    G_comp = np.full(G.shape, 0)

    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            G_comp[i, j] = 1 if G[i, j] == 0 else 0

    return G_comp


def transpose(G):
    """
    Algorithme calculant la matrice d'adjacence du graphe transposé.

    Complexité:
        - O(n^2)

    Argument:
        - G (numpy.array): La matrice d'adjacence du graphe.

    Return:
        - G_T (numpy.array): La matrice d'adjacence du graphe transposé.
    """
    G_T = np.full(G.shape, 0)

    for i in range(G.shape[0]):
        for j in range(G.shape[1]):
            if G[i, j] == 1:
                G_T[j, i] = 1

    return G_T
