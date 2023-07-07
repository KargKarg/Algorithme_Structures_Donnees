def appartient(arr, objet):
    for i in range(arr.fin + 1):
        if arr.vue[i] == objet:
            return True
    return False
