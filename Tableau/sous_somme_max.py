from sous_somme import sous_somme


def sous_somme_max(arr):
    maxi = arr.vue[arr.fin]
    max_g, max_d = 0, 0

    for g in range(arr.fin+1):
        for d in range(g+1, arr.fin+1):
            ss_somme = sous_somme(arr, g, d)
            if ss_somme > maxi:
                maxi = ss_somme
                max_g, max_d = g, d

    return maxi, max_g, max_d
