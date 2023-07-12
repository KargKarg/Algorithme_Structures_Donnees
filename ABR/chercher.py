def chercher(noeud, entier: int) -> bool:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.
        - entier (int): l'entier a inséré dans l'ABR.

    Retours:
        - True: si l'entier est dans l'ABR.
        - False: si non.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui recherche un entier dans un ABR.

    """
    if noeud is None:
        return False
    elif noeud.valeur == entier:
        return True
    elif noeud.valeur < entier:
        return chercher(noeud.droite, entier)
    else:
        return chercher(noeud.gauche, entier)
