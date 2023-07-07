from Structures import tableau
from inserer import inserer


def sans_doublons(arr):
    sd_arr = tableau.Tableau(arr.nmax)
    for i in range(arr.fin+1):
        contenu = False
        for j in range(i+1, arr.fin+1):
            if arr.vue[i] == arr.vue[j]:
                contenu = True
                break
        if not contenu:
            inserer(sd_arr, arr.vue[i])

    arr.vue = sd_arr.vue
    arr.fin = sd_arr.fin
    del sd_arr
