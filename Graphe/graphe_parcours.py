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
            for j in range(G.shape[1]):
                if G[elem - 1, j] == 1 and etat[j] is None:
                    file_ajouter.ajouter(q, j + 1)
                    etat[j] = 'vu'
                    pere[j] = elem

    return pere


def profondeur(path: str, debut: int, oriente: bool = True) -> tuple:
    """
    Algorithme permettant le parcours en profondeur d'un graphe.
    Il considérera les sommets dans par un ordre croissant.

    Complexité:
        - O(n)

    Argument:
        - path (str): Chemin vers le graphe au format texte.
        - debut (int): Début du parcours en profondeur.
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


def profondeur_date(G) -> tuple:
    """
    Algorithme de calcul d'un parcours en profondeur daté.
    Les sommets sont considérés dans l'ordre croissant.

    Complexité:
        - O(n)

    Argument:
        - G (numpy.array): La matrice d'adjacence du graphe.

    Retour:
        - premiere_date (list): La liste des premières dates.
        -> premiere_date[i]: La première date de i.
        - derniere_date (list): La liste des dernières dates.
        -> dernière_date[i]: La dernière date de i.
    """
    sommet, date = 1, 0
    etat = [None for _ in range(G.shape[0])]
    premiere_date, derniere_date = [None for _ in range(G.shape[0])], [None for _ in range(G.shape[0])]

    def parcours(G, sommet: int, date: int, etat: list, premiere_date: list, derniere_date: list):
        """
        Algorithme de parcours en profondeur récursif mettant à jour les dates et les états.

        Argument:
            - G (numpy.array): La matrice d'adjacence du graphe.
            - sommet (int): Le sommet considéré.
            - date (int): La date du parcours.
            - etat (list): La liste contenant les états des sommets.
            - premiere_date (list): La liste contenant les premières dates des sommets.
            - derniere_date (list): La liste contenant les dernières dates des sommets.

        Return:
            - date (int): La dernière date du sommet.
        """
        date += 1
        etat[sommet - 1], premiere_date[sommet - 1] = 'vu', date

        for j in range(G.shape[1]):
            if G[sommet - 1, j] == 1 and etat[j] is None:
                date = parcours(G, j + 1, date, etat, premiere_date, derniere_date)

        date += 1
        derniere_date[sommet - 1] = date

        return date

    date = parcours(G, sommet, date, etat, premiere_date, derniere_date)

    suivant = 0

    while None in etat:
        suivant += 1
        if etat[suivant-1] is None:
            parcours(G, suivant, date, etat, premiere_date, derniere_date)

    return premiere_date, derniere_date
