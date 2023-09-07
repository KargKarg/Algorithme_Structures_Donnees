from Structures import arbre


def inserer_feuille(noeud, entier: int) -> None:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.
        - entier (int): l'entier a inséré dans l'ABR.

    Retours:
        - None.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui ajoute aux feuilles l'entier.

    """
    if entier <= noeud.valeur and noeud.gauche is None:
        gauche = arbre.ABR(entier)
        noeud.gauche = gauche
    elif entier <= noeud.valeur:
        inserer_feuille(noeud.gauche, entier)
    elif entier > noeud.valeur and noeud.droite is None:
        droite = arbre.ABR(entier)
        noeud.droite = droite
    else:
        inserer_feuille(noeud.droite, entier)
