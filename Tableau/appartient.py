def appartient(arr, entier):
    for i in range(arr.fin + 1):
        if arr.vue[i] == entier:
            return True
    return False
