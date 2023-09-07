from abr_chercher import chercher


def est_contenu(noeud1, noeud2) -> bool:
    """
    Arguments:
        - noeud1 (instance): arbre créé par la classe Arbre.
        - noeud2 (instance): arbre créé par la classe Arbre.

    Retours:
        - True: noeud1 est contenu dans noeud2.
        - False: si non.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui teste si noeud1 est contenu dans noeud2.

    """
    if noeud1 is None:
        return True
    elif noeud1.gauche is None and noeud1.droite is None:
        return chercher(noeud2, noeud1.valeur)
    elif noeud1.gauche is not None and noeud1.droite is None:
        return chercher(noeud2, noeud1.valeur) and est_contenu(noeud1.gauche, noeud2)
    elif noeud1.gauche is None and noeud1.droite is None:
        return chercher(noeud2, noeud1.valeur) and est_contenu(noeud1.droite, noeud2)
    else:
        return chercher(noeud2, noeud1.valeur) and est_contenu(noeud1.gauche, noeud2) and est_contenu(noeud1.droite, noeud2)
