import math


def maximum_unimodal(arr) -> int:
    """
    Arguments:
        - arr (instance): tableau unimodal crée par la classe Tableau.

    Retours:
        - (int): l'entier maximum du tableau unimodal.

    Complexité:
        - 0(N*log2(N))

    Résumé:
        Fonction recherche l'élément maximum d'un tableau unimodal par dichotomie.

    """
    g = 0
    d = arr.fin
    m = math.ceil((g+d)/2)

    while m != d and m != g:
        if arr.vue[m] < arr.vue[m+1]:
            g = m
            m = math.ceil((g+d)/2)
        else:
            d = m
            m = math.ceil((g+d)/2)

    return arr.vue[m]
