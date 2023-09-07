def vide(liste):
    """
    Arguments:
        - liste (instance): liste chaînée créée par la classe Liste.

    Retours:
        - True: si la liste chaînéee est vide.
        - False: si non.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui teste si une liste chaînée est vide.

    """
    if len(liste.vue) == 0:
        return True
    else:
        return False
