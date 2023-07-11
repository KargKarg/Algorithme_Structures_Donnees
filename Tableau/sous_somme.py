def sous_somme(arr, g, d):
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.
        - g (int): l'indice délimitant le bord gauche du sous-tableau.
        - d (int): l'indice délimitant le bord droit du sous-tableau.

    Retours:
        - ss_somme (int); la sous-somme du sous-tableau.

    Complexité:
        - 0(n)

    Résumé:
        Fonction qui parcours l'ensemble du tableau pour évaluer la somme entre les indices [g, d].

    """
    ss_somme = 0
    for i in range(g, d+1):
        ss_somme += arr.vue[i]
    return ss_somme
