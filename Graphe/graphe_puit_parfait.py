import numpy as np
from Graphe import graphe_lecture


def puit(path: str) -> int or bool:
    """
    Algorithme cherchant un puit parfait dans le graphe orienté.
    Si il n'existe pas, renvoie alors le puit parfait possible en retirant/ajoutant le minimum d'arcs.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.

    Return:
        Si source parfaite:
            - (int): Correpondant au sommet étant un puit parfait.

        Sinon:
            - False (bool)
            - pot_src (int): Correspondant au sommet pouvant être un puit parfait si arcs retirés.
            - ajouter (set): Le nombre d'arcs à ajouter.
            - supprimer (set): Le nombre d'arcs à supprimer.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path)
    ajouter, supprimer, minimum, pot_puit = set(), set(), np.inf, 0

    for i in range(G.shape[0]):
        local_supprimer, local_ajouter = set(), set()
        pt = True
        for j in range(G.shape[1]):

            if i != j and G[i, j] == 1:
                pt = False
                local_supprimer.add((i+1, j+1))

            if i != j and G[j, i] == 0:
                pt = False
                local_ajouter.add((j+1, i+1))

        if pt:
            return i+1

        elif not pt and len(local_ajouter) + len(local_supprimer) < minimum:
            ajouter, supprimer, minimum = local_ajouter, local_supprimer, len(local_ajouter) + len(local_supprimer)
            pot_puit = i+1

    return False, pot_puit, ajouter, supprimer
