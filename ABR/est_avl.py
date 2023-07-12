from desequilibre import desequilibre


def est_avl(noeud) -> bool:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - True: si l'ABR est un AVL.
        - False: si non.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui teste si un ABR est un AVL.
    """
    if noeud.gauche is None and noeud.droite is None:
        return True
    elif noeud.gauche is not None and noeud.droite is None and -1 <= desequilibre(noeud) <= 1:
        return est_avl(noeud.gauche)
    elif noeud.gauche is None and noeud.droite is not None and -1 <= desequilibre(noeud) <= 1:
        return est_avl(noeud.droite)
    elif noeud.gauche is not None and noeud.droite is not None and -1 <= desequilibre(noeud) <= 1:
        return est_avl(noeud.gauche) and est_avl(noeud.droite)
    else:
        return False
