from Structures import tableau
from inserer import inserer
from min_max import min_et_max


def tri_denombrement(arr) -> None:
    """
    Arguments:
        - arr (instance): tableau crée par la classe Tableau.

    Retours:
        - None.

    Complexité:
        - O(n^2)

    Résumé:
        Fonction qui tri le tableau à l'aide d'un deuxième tableau qui permettra de dénombrer les entiers.
        Fonctionne plutôt bien lorsque le maximum d'une tableau n'est pas une valeur très grande.

    """
    compte = tableau.Tableau(min_et_max(arr)[1]+1)

    for i in range(compte.nmax):
        inserer(compte, 0)

    tri = tableau.Tableau(arr.nmax)

    for i in range(arr.fin+1):
        compte.vue[arr.vue[i]] += 1

    for i in range(compte.fin+1):
        for j in range(compte.vue[i]):
            inserer(tri, i)

    arr.vue = tri.vue
    arr.fin = tri.fin

    del tri, compte
