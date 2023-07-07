from Structures import tableau
from inserer import inserer
from min_max import min_et_max


def tri_denombrement(arr):
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
