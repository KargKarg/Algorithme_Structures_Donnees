from Structures import pile
from Pile import empiler, depiler, pile_vide
from Graphe import graphe_lecture


def profondeur(path: str) -> int:
    """
    Algorithme calculant le nombre de composantes connexes.

    Complexité:
        - O(n)

    Argument:
        - path (str): Chemin vers le graphe au format texte.

    Return:
        - composante (int): Le nombre de composantes connexes.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, False)
    p = pile.Pile(G.shape[0])
    etat = [None for _ in range(G.shape[0])]

    empiler.empiler(p, 1)

    sommet = 1

    composante = 1

    while sommet <= G.shape[0]:
        if etat[sommet - 1] is not None:
            sommet += 1
        elif pile_vide.vide(p):
            empiler.empiler(p, sommet)
            composante += 1
        while not pile_vide.vide(p):
            elem = depiler.depiler(p)
            if etat[elem-1] is None:
                etat[elem-1] = 'vu'
                for j in range(G.shape[1]-1, -1, -1):
                    if G[elem - 1, j] == 1 and etat[j] is None:
                        empiler.empiler(p, j + 1)
    return composante
