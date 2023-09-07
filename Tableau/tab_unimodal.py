def unimodal(arr) -> bool:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.

    Retours:
        - True: si le tableau est unimodal.
        - False: si non.

    Complexité:
        - O(n)

    Résumé:
        Fonction qui teste si le tableau est unimodal.

    """
    variation = 0
    for i in range(arr.fin):
        if arr.vue[i] > arr.vue[i+1] and variation == 0:
            variation += 1
        elif arr.vue[i] < arr.vue[i+1] and variation > 0:
            return False
    return True
