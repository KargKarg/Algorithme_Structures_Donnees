def est_abr(noeud) -> bool:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - True: si l'arbre est un ABR.
        - False: si non.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui teste si l'arbre est un ABR.
    """
    if noeud.gauche is None and noeud.droite is None:
        return True
    elif noeud.gauche is None and noeud.droite is not None:
        if noeud.valeur < noeud.droite.valeur:
            return est_abr(noeud.droite)
    elif noeud.droite is None and noeud.gauche is not None:
        if noeud.gauche.valeur <= noeud.valeur:
            return est_abr(noeud.gauche)
    else:
        if noeud.gauche.valeur <= noeud.valeur < noeud.droite.valeur:
            return est_abr(noeud.droite) and est_abr(noeud.gauche)
