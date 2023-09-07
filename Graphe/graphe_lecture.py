import numpy as np


def matrice_adjacence(path: str, oriente: bool = True, pondere: bool = False) -> tuple:
    """
    Algorithme permettant de calculer la matrice d'adjacence d'un graphe à partir du format:

        |V|
        V1;V2;poids
        V2;V3;poids
        Vn;Vn-1,poids

        avec |V| = n

    Complexité:
        - 0(n)

    Argument:
        - path (str): Chemin vers le fichier texte.
        - oriente (bool): Vrai si le graphe doit être orienté, Faux sinon.
        - pondere (bool): Vrai si le graphe doit être pondéré, Faux sinon.

    Return:
        - matrice_adj (np.array): Matrice d'adjacence du graphe.
        - matrice_poids (np.array): Matrice de poids du graphe.
        - sommets (set): Ensemble des sommets du graphe.
        - arcs/aretes (set): Ensemble des arcs/aretes du graphe.
    """
    with open(path, 'r') as fil:
        card_sommet = int(fil.readline())
        matrice_adj = np.full((card_sommet, card_sommet), 0, int)
        sommets = set()

        if pondere:

            matrice_poids = np.full((card_sommet, card_sommet), np.inf)

            if oriente:

                arcs = set()

                for ligne in fil:
                    predecesseur, successeur, poids = list(map(int, ligne.split(';')))

                    matrice_adj[predecesseur-1, successeur-1] = 1
                    matrice_poids[predecesseur-1, successeur-1] = poids

                    sommets = sommets.union({predecesseur, successeur})
                    arcs.add((predecesseur, successeur))

                return matrice_adj, matrice_poids, sommets, arcs

            elif not oriente:

                aretes = set()

                for ligne in fil:
                    voisin1, voisin2, poids = list(map(int, ligne.split(';')))

                    matrice_adj[voisin1-1, voisin2-1] = 1
                    matrice_adj[voisin2-1, voisin1-1] = 1
                    matrice_poids[voisin1-1, voisin2-1] = poids
                    matrice_poids[voisin2-1, voisin1-1] = poids

                    sommets = sommets.union({voisin1, voisin2})
                    aretes.add((voisin1, voisin2))
                    aretes.add((voisin2, voisin1))

                return matrice_adj, matrice_poids, sommets, aretes

        elif not pondere:

            if oriente:

                arcs = set()

                for ligne in fil:
                    predecesseur, successeur = list(map(int, ligne.split(';')))

                    matrice_adj[predecesseur - 1, successeur - 1] = 1

                    sommets = sommets.union({predecesseur, successeur})
                    arcs.add((predecesseur, successeur))

                return matrice_adj, sommets, arcs

            if not oriente:

                aretes = set()

                for ligne in fil:
                    voisin1, voisin2 = list(map(int, ligne.split(';')))

                    matrice_adj[voisin1 - 1, voisin2 - 1] = 1
                    matrice_adj[voisin2 - 1, voisin1 - 1] = 1

                    sommets = sommets.union({voisin1, voisin2})
                    aretes.add((voisin1, voisin2))
                    aretes.add((voisin2, voisin1))

                return matrice_adj, sommets, aretes
