from chercher import chercher


def supprimer(liste, objet: any) -> bool:
    """
    Arguments:
        - liste (instance): liste chaînée créée par la classe Liste.
        - objet (any): élément à supprimer dans la liste chaînée.

    Retours:
        - True: si l'élément n'est plus dans la liste chaînée.
        - False: si il n'y était pas.

    Complexité:
        - O(N)

    Résumé:
        Fonction qui supprime un élément dans une liste chaînée.

    """
    indice = chercher(liste, objet)
    if indice is not None:
        g = liste.vue[:indice]
        d = liste.vue[indice+1:]
        liste.vue = g + d
        return True
    else:
        return False
