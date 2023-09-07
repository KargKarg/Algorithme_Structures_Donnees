from abr_est_contenu import est_contenu


def egaux(noeud1, noeud2) -> bool:
    """
    Arguments:
        - noeud1 (instance): arbre créé par la classe Arbre.
        - noeud2 (instance): arbre créé par la classe Arbre.

    Retours:
        - True: noeud1 = noeud2.
        - False: si non.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui teste si noeud1 est égal à noeud2.

    """
    return est_contenu(noeud1, noeud2) and est_contenu(noeud2, noeud1)
