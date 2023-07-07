def inserer(arr, objet):
    if arr.fin == arr.nmax - 1:
        return False
    else:
        arr.vue[arr.fin + 1] = objet
        arr.fin += 1
        return True
