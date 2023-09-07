from abr_noeuds import nb_noeuds


def descendants(noeud) -> int:
    """
    Arguments:
        - noeud (instance): arbre créé par la classe Arbre.

    Retours:
        - (int): le nombre de descendants.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui calcule le nombre de descendants d'un noeud.

    """
    return nb_noeuds(noeud) - 1
