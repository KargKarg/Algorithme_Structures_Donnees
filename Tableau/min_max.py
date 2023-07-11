def min_et_max(arr) -> tuple:
    """
    Arguments:
        - arr (instance): tableau crée par la classe Tableau.

    Retours:
        - (tuple): le minimum, le maxium du tableau

    Complexité:
        - O(n)

    Résumé:
        Fonction qui parcours l'ensemble du tableau pour comparer chaque élément avec le maximum, puis le minimum.

    """
    mini = arr.vue[0]
    maxi = arr.vue[0]
    for i in range(arr.fin + 1):
        if arr.vue[i] > maxi:
            maxi = arr.vue[i]
        elif arr.vue[i] < mini:
            mini = arr.vue[i]
    return mini, maxi
