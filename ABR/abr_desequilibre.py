from abr_hauteur import hauteur


def desequilibre(noeud) -> int:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): hauteur(sous-arbre-gauche) -- hauteur(sous-arbre-droit) = déséquilibre

    Complexité:
        - O(N)

    Résumé:
        Fonction qui calcule le déséquilibre d'un noeud.
    """
    if noeud is None:
        return 0
    else:
        return hauteur(noeud.gauche) - hauteur(noeud.droite)
