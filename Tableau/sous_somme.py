def sous_somme(arr, g, d):
    ss_somme = 0
    for i in range(g, d+1):
        ss_somme += arr.vue[i]
    return ss_somme
