def strahler(noeud) -> int:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): le nombre de Strahler de l'arbre.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui calcule le nombre de Strahler de l'arbre.
    """
    if noeud is None:
        return 0
    str_sag = strahler(noeud.gauche)
    str_sad = strahler(noeud.droite)
    if str_sag == str_sad:
        return 1 + str_sad
    else:
        return max(str_sag, str_sad)