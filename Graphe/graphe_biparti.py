from Structures import file
from File import file_ajouter, file_supprimer, file_vide
from Graphe import graphe_lecture


def biparti(path: str, oriente: bool = True) -> bool:
    """
    Algorithme permettant de tester si un graphe est biparti.

    Complexité:
        - O(n)

    Argument:
        - path (str): Chemin vers le graphe au format texte.
        - oriente (bool): Vrai si le graphe est oriente, Faux sinon.

    Return:
        - (bool): Vrai si le graphe est biparti, Faux sinon.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, oriente)
    q = file.File(G.shape[0])
    etat = [None for _ in range(G.shape[0])]
    pere = [None for _ in range(G.shape[0])]
    couleur = [0 for _ in range(G.shape[0])]

    file_ajouter.ajouter(q, 1)
    etat[0] = 'vu'
    couleur[0] = 1

    sommet = 1

    while sommet <= G.shape[0]:
        if etat[sommet-1] is not None:
            sommet += 1
        elif file_vide.vide(q):
            file_ajouter.ajouter(q, sommet)
            etat[sommet-1] = 'vu'
            couleur[sommet-1] = 1
        while not file_vide.vide(q):
            elem = file_supprimer.supprimer(q)
            for j in range(G.shape[1]):
                if G[elem - 1, j] == 1 and etat[j] is None:
                    file_ajouter.ajouter(q, j + 1)
                    etat[j] = 'vu'
                    pere[j] = elem
                    couleur[j] = 3 - couleur[elem-1]
                elif G[elem - 1, j] == 1 and etat[j] is not None and couleur[elem-1] == couleur[j]:
                    return False

    return True
