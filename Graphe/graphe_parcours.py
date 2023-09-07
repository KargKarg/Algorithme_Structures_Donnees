from Structures import file, pile
from File import file_ajouter, file_supprimer, file_vide
from Pile import empiler, depiler, pile_vide
from Graphe import graphe_lecture


def largeur(path: str, debut: int, oriente: bool = True) -> list:
    """
    Algorithme permettant le parcours en largeur d'un graphe.
    Il considérera les sommets dans par un ordre croissant.

    Complexité:
        - O(n)

    Argument:
        - path (str): Chemin vers le graphe au format texte.
        - debut (int): Début du parcours en largeur.
        - oriente (bool): Vrai si le graphe est oriente, Faux sinon.

    Return:
        - pere (list): Arborescence du parcours en largeur. Les racines ont 'None' pour père.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, oriente)
    q = file.File(G.shape[0])
    etat = [None for _ in range(G.shape[0])]
    pere = [None for _ in range(G.shape[0])]

    file_ajouter.ajouter(q, debut)
    etat[debut-1] = 'vu'

    sommet = 1

    while sommet <= G.shape[0]:
        if etat[sommet-1] is not None:
            sommet += 1
        elif file_vide.vide(q):
            file_ajouter.ajouter(q, sommet)
            etat[sommet-1] = 'vu'
        while not file_vide.vide(q):
            elem = file_supprimer.supprimer(q)
            for j in range(G.shape[0]):
                if G[elem - 1, j] == 1 and etat[j] is None:
                    file_ajouter.ajouter(q, j + 1)
                    etat[j] = 'vu'
                    pere[j] = elem

    return pere


def profondeur(path: str, debut: int, oriente: bool = True) -> list:
    """
    Algorithme permettant le parcours en profondeur d'un graphe.
    Il considérera les sommets dans par un ordre croissant.

    Complexité:
        - O(n)

    Argument:
        - path (str): Chemin vers le graphe au format texte.
        - debut (int): Début du parcours en largeur.
        - oriente (bool): Vrai si le graphe est oriente, Faux sinon.

    Return:
        - pere (list): Arborescence du parcours en profondeur. Les racines ont 'None' pour père.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, oriente)
    p = pile.Pile(G.shape[0])
    etat = [None for _ in range(G.shape[0])]
    pere = [None for _ in range(G.shape[0])]
    dernier_pred = [None for _ in range(G.shape[0])]

    empiler.empiler(p, debut)

    sommet = 1

    while sommet <= G.shape[0]:
        if etat[sommet - 1] is not None:
            sommet += 1
        elif pile_vide.vide(p):
            empiler.empiler(p, sommet)
        while not pile_vide.vide(p):
            elem = depiler.depiler(p)
            if etat[elem-1] is None:
                etat[elem-1] = 'vu'
                pere[elem-1] = dernier_pred[elem-1]
                for j in range(G.shape[0]-1, -1, -1):
                    if G[elem - 1, j] == 1 and etat[j] is None:
                        empiler.empiler(p, j + 1)
                        dernier_pred[j] = elem
    return pere
