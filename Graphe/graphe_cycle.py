from Structures import pile
from Pile import empiler, depiler, pile_vide


def cycle(G) -> bool:
    """
        Algorithme permettant de détecter si un cycle est présent dans le graphe.

        Complexité:
            - O(n)

        Argument:
            - G (numpy.array): La matrice d'adjacence du graphe.

        Return:
            - (bool): Vrai si le graphe contient un cycle, Faux sinon.
        """
    p = pile.Pile(G.shape[0])
    etat = [None for _ in range(G.shape[0])]
    pere = [None for _ in range(G.shape[0])]
    dernier_pred = [None for _ in range(G.shape[0])]

    empiler.empiler(p, 1)

    sommet = 1

    while sommet <= G.shape[0]:
        if etat[sommet - 1] is not None:
            sommet += 1
        elif pile_vide.vide(p):
            empiler.empiler(p, sommet)
        while not pile_vide.vide(p):
            elem = depiler.depiler(p)
            if etat[elem - 1] is None:
                etat[elem - 1] = 'vu'
                pere[elem - 1] = dernier_pred[elem - 1]
                for j in range(G.shape[0] - 1, -1, -1):
                    if G[elem - 1, j] == 1 and etat[j] is None:
                        empiler.empiler(p, j + 1)
                        dernier_pred[j] = elem
            else:
                return True
    return False
