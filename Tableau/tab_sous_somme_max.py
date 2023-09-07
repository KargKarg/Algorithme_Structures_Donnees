from tab_sous_somme import sous_somme


def sous_somme_max(arr) -> tuple:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.

    Retours:
        - maxi (int): la sous-somme maximale.
        - max_g (int): l'indice de gauche du sous-tableau.
        - max_d (int): l'indice de droite du sous-tableau.

    Complexité:
        - O(n^2)

    Résumé:
        Fonction calcule la sous-somme maximale d'un tableau et renvoie sa valeur ainsi que les indices du sous-tableau.

    """
    maxi = arr.vue[arr.fin]
    max_g, max_d = 0, 0

    for g in range(arr.fin+1):
        for d in range(g+1, arr.fin+1):
            ss_somme = sous_somme(arr, g, d)
            if ss_somme > maxi:
                maxi = ss_somme
                max_g, max_d = g, d

    return maxi, max_g, max_d
