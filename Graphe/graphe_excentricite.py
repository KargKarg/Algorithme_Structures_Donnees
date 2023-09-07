from Structures import file
from File import file_ajouter, file_supprimer, file_vide
from Graphe import graphe_lecture


def excentricite_sommet(G, debut: int) -> int:
    """
    Algorithme de calcul d'excentricté un sommet.

    Complexité:
        - O(n)

    Argument:
        - G (np.array): La matrice d'adjacence du graphe.
        - debut (int): Le sommet considéré.

    Return:
        - max(hauteur) (int): Correspond à l'excentricité du sommet.
    """
    q = file.File(G.shape[0])
    etat = [None for _ in range(G.shape[0])]
    pere = [None for _ in range(G.shape[0])]
    hauteur = [0 for _ in range(G.shape[0])]

    file_ajouter.ajouter(q, debut)
    etat[debut - 1] = 'vu'

    sommet = 1

    while sommet <= G.shape[0]:
        if etat[sommet - 1] is not None:
            sommet += 1
        elif file_vide.vide(q):
            file_ajouter.ajouter(q, sommet)
            etat[sommet - 1] = 'vu'
        while not file_vide.vide(q):
            elem = file_supprimer.supprimer(q)
            for j in range(G.shape[1]):
                if G[elem - 1, j] == 1 and etat[j] is None:
                    file_ajouter.ajouter(q, j + 1)
                    etat[j] = 'vu'
                    pere[j] = elem
                    hauteur[j] = hauteur[elem-1] + 1

    return max(hauteur)


def excentricite_graphe(path: str, oriente: bool = True) -> list:
    """
    Algorithme de calcul d'excentricté pour chaque sommet du graphe.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Le chemin vers le graphe sous format txt.
        - oriente (bool): Vrai si le graphe est orienté, Faux sinon.

    Return:
        - excentricites (list): Correspond à l'excentricité de chaque sommet.
        -> excentricites[i]: Correspond à l'excentricité du sommet i.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, oriente)
    excentricites = [0 for _ in range(G.shape[0])]

    for i in range(G.shape[0]):
        excentricites[i] = excentricite_sommet(G, i+1)

    return excentricites
