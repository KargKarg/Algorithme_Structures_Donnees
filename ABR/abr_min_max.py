def min_max(noeud) -> tuple:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): le minimum.
        - (int): le maximum.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui trouve respectivement le minimum et le maximum de l'ABR.

    """
    if noeud.gauche is None and noeud.droite is None:
        return noeud.valeur, noeud.valeur
    elif noeud.gauche is not None and noeud.droite is None:
        return min(min_max(noeud.gauche)), noeud.valeur
    elif noeud.gauche is None and noeud.droite is not None:
        return noeud.valeur, max((min_max(noeud.droite)))
    else:
        return min(min_max(noeud.gauche)), max(min_max(noeud.droite))
