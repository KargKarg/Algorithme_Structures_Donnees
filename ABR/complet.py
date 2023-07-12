from hauteur import hauteur
from noeuds import nb_noeuds


def est_complet(noeud) -> bool:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - True: si l'arbre est complet.
        - False: si non.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui teste si un arbre est complet.

    """
    h = hauteur(noeud)
    d = nb_noeuds(noeud) - 1
    if d+1 == pow(2, h+1) - 1:
        return True
    else:
        return False
