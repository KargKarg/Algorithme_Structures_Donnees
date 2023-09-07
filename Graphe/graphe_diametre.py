from Graphe import graphe_excentricite
from Graphe import graphe_lecture


def diametre(path: str, oriente: bool = True) -> int:
    """
    Algorithme de calcul du diamètre d'un graphe.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format txt.
        - oriente (bool): Vrai si le graphe est orienté, Faux sinon.

    Return:
        - max(excentricites) (int): Correspond au diamètre du graphe.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, oriente)

    return max(graphe_excentricite.excentricite_graphe(path, oriente))
