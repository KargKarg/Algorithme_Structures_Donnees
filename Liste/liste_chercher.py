from Structures import listech


def chercher(liste, objet: any) -> int or False:
    """
    Arguments:
        - liste (instance): liste chaînée créée par la classe Liste.
        - objet (any): élément à rechercher dans la liste chaînée.

    Retours:
        - cpt (int): correspond à sa place dans la liste chaînée.
        - False: l'élément n'ai pas dans la liste

    Complexité:
        - O(N)

    Résumé:
        Fonction qui recherche un élément dans une liste chaînée.

    """
    cpt = 0
    while len(liste.vue[cpt:]) != 0 and liste.vue[cpt] != objet:
        cpt += 1
    if len(liste.vue[cpt:]) == 0:
        return False
    else:
        return cpt
