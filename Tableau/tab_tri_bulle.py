def tri_bulle(arr) -> None:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.

    Retours:
        - None

    Complexité:
        - O(n^2)

    Résumé:
        Fonction qui tri le tableau à l'aide du tri à bulle, une étape a été rajouté pour '''améliorer''' la compléxité.

    """
    for i in range(arr.fin+1):
        switch = False
        for j in range(arr.fin, i, -1):
            if arr.vue[j-1] > arr.vue[j]:
                flag = arr.vue[j-1]
                arr.vue[j-1] = arr.vue[j]
                arr.vue[j] = flag
                switch = True
        if not switch:
            break
