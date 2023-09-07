from Graphe import graphe_parcours
from Graphe import graphe_lecture


def points_articulations(path: str) -> set:
    """
    Algorithme calculant les points d'articulations d'un graphe non oreinté.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe au format texte.

    Return:
        - arts (set): L'ensemble des points d'articulations du graphe.
    """
    arts = set()
    _, V, _ = graphe_lecture.matrice_adjacence(path, False)

    for sommet in V:
        arborescence = graphe_parcours.profondeur(path, sommet, False)
        if arborescence.count(sommet) > 1:
            arts.add(sommet)

    return arts
