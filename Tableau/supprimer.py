def supprimer(arr, entier):
    for i in range(arr.fin+1):
        if arr.vue[i] == entier:
            for j in range(i+1, arr.fin+2):
                arr.vue[j-1] = arr.vue[j]
            arr.fin -= 1
            break
