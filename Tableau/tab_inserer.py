def inserer(arr, objet: any) -> bool:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.
        - objet (any): élément de n'importe quel type.

    Retours:
        - True: si l'élément est inséré.
        - Faux: si le tableau est plein.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui ajoute l'élément à la fin du tableau.

    """
    if arr.fin == arr.nmax - 1:
        return False
    else:
        arr.vue[arr.fin + 1] = objet
        arr.fin += 1
        return True
