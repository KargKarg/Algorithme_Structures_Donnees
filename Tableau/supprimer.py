def supprimer(arr, objet: any) -> bool:
    """
    Arguments:
        - arr (instance): tableau crée par la classe Tableau.
        - objet (any): élément à retirer du tableau.

    Retours:
        - True: si l'objet est dans le tableau.
        - False: si non.

    Complexité:
        - O(n)

    Résumé:
        Fonction supprime un objet du tableau.

    """
    for i in range(arr.fin+1):
        if arr.vue[i] == objet:
            for j in range(i+1, arr.fin+2):
                arr.vue[j-1] = arr.vue[j]
            arr.fin -= 1
            return True
    return False
