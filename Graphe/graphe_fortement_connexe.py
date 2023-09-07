from Graphe import graphe_transformation
from Graphe import graphe_lecture
from Graphe import graphe_parcours
from Structures import pile
from Pile import empiler, depiler, pile_vide
import numpy as np


def profondeur_sommet(G, debut: int, etat: list, dernieres_dates: list, ens_comp: set) -> tuple:
    """
    Algorithme permettant le parcours en profondeur d'un sommet.

    Complexité:
        - O(n)

    Argument:
        - G (numpy,array): La matrice d'adjacence du graphe.
        - debut (int): Début du parcours en profondeur.
        - etat (list): Liste contenant l'états des sommets.
        - dernieres_dates (list): Liste contenant les dernieres dates des sommets.
        - ens_comp (set): Ensemble contenant les composantes fortemement connexes.

    Return:
        - etat (list): Liste contenant l'états des sommets.
        - ens_comp (set): Ensemble contenant les composantes fortemement connexes.
    """
    comp = tuple()
    p = pile.Pile(G.shape[0])

    empiler.empiler(p, debut)

    while not pile_vide.vide(p):
        elem = depiler.depiler(p)
        dernieres_dates[elem-1] = -np.inf
        if etat[elem-1] is None:
            etat[elem-1] = 'vu'
            comp += (elem,)
            for j in range(G.shape[0]-1, -1, -1):
                if G[elem - 1, j] == 1 and etat[j] is None:
                    empiler.empiler(p, j + 1)
    ens_comp.add(comp)
    return etat, ens_comp


def composante(path: str) -> tuple:
    """
    Algorithme permettant le parcours en profondeur d'un sommet.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.

    Return:
        - len(ens_comp) (int): Le nombre de composantes fortement connexes.
        - ens_comp (set): Ensemble contenant les composantes fortemement connexes.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path)
    G_T = graphe_transformation.transpose(G)
    _, dernieres_dates = graphe_parcours.profondeur_date(G)

    ens_comp = set()

    etat = [None for _ in range(G.shape[0])]

    maxi = dernieres_dates.index(max(dernieres_dates))

    while dernieres_dates[maxi] != -np.inf:
        etat, ens_comp = profondeur_sommet(G_T, maxi+1, etat, dernieres_dates, ens_comp)
        maxi = dernieres_dates.index(max(dernieres_dates))

    return len(ens_comp), ens_comp
