def appartient(arr, objet: any) -> bool:
    """
    Arguments:
        - arr (instance): tableau crée par la classe Tableau.
        - objet (any): élément de n'importe quel type.

    Retours:
        - True: si l'élément est dans le tableau.
        - Faux: si non.

    Complexité:
        - O(n)

    Résumé:
        Fonction qui parcours l'ensemble du tableau pour comparer chaque élément avec l'objet passé en argument,
        si l'élément est l'objet qu'on recherche, cela s'arrête.

    """
    for i in range(arr.fin + 1):
        if arr.vue[i] == objet:
            return True
    return False
