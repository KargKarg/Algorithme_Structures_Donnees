import numpy as np
from Graphe import graphe_lecture


def source(path: str) -> int or tuple:
    """
    Algorithme cherchant une source parfaite dans le graphe orienté.
    Si elle n'existe pas, renvoie alors la source parfaite possible en retirant/ajoutant le minimum d'arcs.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.

    Return:
        Si source parfaite:
            - (int): Correpondant au sommet étant une source parfaite.

        Sinon:
            - False (bool)
            - pot_src (int): Correspondant au sommet pouvant être une source parfaite si arcs retirés.
            - ajouter (set): Le nombre d'arcs à ajouter.
            - supprimer (set): Le nombre d'arcs à supprimer.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path)
    ajouter, supprimer, minimum, pot_src = set(), set(), np.inf, 0

    for i in range(G.shape[0]):
        local_supprimer, local_ajouter = set(), set()
        src = True
        for j in range(G.shape[1]):

            if i != j and G[i, j] == 0:
                src = False
                local_ajouter.add((i+1, j+1))

            if i != j and G[j, i] == 1:
                src = False
                local_supprimer.add((j+1, i+1))

        if src:
            return i+1

        elif not src and len(local_ajouter) + len(local_supprimer) < minimum:
            ajouter, supprimer, minimum = local_ajouter, local_supprimer, len(local_ajouter) + len(local_supprimer)
            pot_src = i+1

    return False, pot_src, ajouter, supprimer
