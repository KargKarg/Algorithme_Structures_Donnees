def tri_selection(arr):

    for i in range(arr.fin):
        minimum = i
        for j in range(i+1, arr.fin+1):
            if arr.vue[minimum] > arr.vue[j]:
                minimum = j
            flag = arr.vue[minimum]
            arr.vue[minimum] = arr.vue[i]
            arr.vue[i] = flag


def tri_selection_recursif(arr, i=0):

    if i == arr.fin+1:
        return

    maximum = i
    for j in range(arr.fin+1):
        if arr.vue[maximum] < arr.vue[j]:
            maximum = j
        flag = arr.vue[maximum]
        arr.vue[maximum] = arr.vue[i]
        arr.vue[i] = flag

    return tri_selection_recursif(arr, i+1)
