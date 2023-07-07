def entasser(arr, indice):
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


def construire_tas(arr):
    for i in range((arr.fin+1)//2, -1, -1):
        entasser(arr, i)
