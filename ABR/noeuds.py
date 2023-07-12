
def nb_noeuds(noeud) -> int:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): le nombre de noeuds de l'arbre.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui calcule le nombre de noeuds de l'arbre.

    """
    if noeud.gauche is None and noeud.droite is None:
        return 1
    elif noeud.gauche is None and noeud.droite is not None:
        return 1 + nb_noeuds(noeud.droite)
    elif noeud.droite is None and noeud.gauche is not None:
        return 1 + nb_noeuds(noeud.gauche)
    else:
        return 1 + nb_noeuds(noeud.gauche) + nb_noeuds(noeud.droite)
