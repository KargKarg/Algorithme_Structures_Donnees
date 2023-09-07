from Graphe import graphe_excentricite
from Graphe import graphe_lecture


def centres(path: str, oriente: bool = True) -> set:
    """
    Algorithme de calcul des centres d'un graphe.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format txt.
        - oriente (bool): Vrai si le graphe est orienté, Faux sinon.

    Return:
        - sommets_centres (set): L'ensemble des centres du graphe.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, oriente)
    sommets_centres = set()

    excentricite = graphe_excentricite.excentricite_graphe(path, oriente)
    minimum = min(excentricite)

    for sommet, exc in enumerate(excentricite):
        if exc == minimum:
            sommets_centres.add(sommet+1)

    return sommets_centres
