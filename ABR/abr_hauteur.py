def hauteur(noeud) -> int:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): hauteur de l'arbre.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui calcule la hauteur d'un arbre.

    """
    if noeud is None:
        return -1
    else:
        return 1 + max(hauteur(noeud.gauche), hauteur(noeud.droite))