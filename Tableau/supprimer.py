def supprimer(arr, objet):
    for i in range(arr.fin+1):
        if arr.vue[i] == objet:
            for j in range(i+1, arr.fin+2):
                arr.vue[j-1] = arr.vue[j]
            arr.fin -= 1
            return True
    return False
