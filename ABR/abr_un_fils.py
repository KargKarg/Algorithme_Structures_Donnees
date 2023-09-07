def un_fils(noeud) -> int:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): le nombre de noeud à un fils.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui calcule le nombre noeud à un fils.

    """
    if noeud.gauche is None and noeud.droite is not None:
        return 1 + un_fils(noeud.droite)

    elif noeud.gauche is not None and noeud.droite is None:
        return 1 + un_fils(noeud.gauche)

    elif noeud.gauche is not None and noeud.droite is not None:
        return 0 + un_fils(noeud.gauche) + un_fils(noeud.droite)

    else:
        return 0
