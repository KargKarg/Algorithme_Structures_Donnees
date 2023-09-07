def tri_selection(arr) -> None:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.

    Retours:
        - None.

    Complexité:
        - O(n^2)

    Résumé:
        Fonction qui tri le tableau avec le tri par séléction.

    """

    for i in range(arr.fin):
        minimum = i
        for j in range(i+1, arr.fin+1):
            if arr.vue[minimum] > arr.vue[j]:
                minimum = j
            flag = arr.vue[minimum]
            arr.vue[minimum] = arr.vue[i]
            arr.vue[i] = flag


def tri_selection_recursif(arr, i: int = 0) -> None:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.
        - i (int): correspond à l'indice du sous-tableau à trier.

    Retours:
        - None.

    Complexité:
        - O(n^2)

    Résumé:
        Fonction qui tri le tableau avec le tri par séléction de manière recursive.

    """
    if i == arr.fin+1:
        return

    maximum = i
    for j in range(arr.fin+1):
        if arr.vue[maximum] < arr.vue[j]:
            maximum = j
        flag = arr.vue[maximum]
        arr.vue[maximum] = arr.vue[i]
        arr.vue[i] = flag

    return tri_selection_recursif(arr, i+1)
