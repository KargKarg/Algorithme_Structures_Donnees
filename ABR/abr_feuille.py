def nb_feuille(noeud) -> int:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): le nombre de descendant de feuille.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui calcule le nombre de feuille d'un arbre.

    """
    if noeud is None:
        return 0
    elif noeud.gauche is None and noeud.droite is None:
        return 1
    else:
        return 0 + nb_feuille(noeud.gauche) + nb_feuille(noeud.droite)
