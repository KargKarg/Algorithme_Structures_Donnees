def entasser(arr, indice: int) -> None:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.
        - indice (int): l'indice correspondant au noeud du tas.

    Retours:
        - None

    Complexité:
        - O(log2(n))

    Résumé:
        Fonction arrange un tableau en tas binaire.

    """
    gauche = 2*indice
    droite = 2*indice+1
    maximum = indice
    if gauche <= arr.fin and arr.vue[gauche] > arr.vue[maximum]:
        maximum = gauche
    if droite <= arr.fin and arr.vue[droite] > arr.vue[maximum]:
        maximum = droite
    if maximum != indice:
        flag = arr.vue[indice]
        arr.vue[indice] = arr.vue[maximum]
        arr.vue[maximum] = flag
        entasser(arr, maximum)


def construire_tas(arr) -> None:
    """
    Arguments:
        - arr (instance): tableau créé par la classe Tableau.

    Retours:
        - None

    Complexité:
        - O(n)

    Résumé:
        Fonction prend un tableau et transforme ce même tableau en tas binaire.

    """
    for i in range((arr.fin+1)//2, -1, -1):
        entasser(arr, i)
