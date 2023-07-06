def min_et_max(arr):
    mini = arr.vue[0]
    maxi = arr.vue[0]
    for i in range(arr.fin + 1):
        if arr.vue[i] > maxi:
            maxi = arr.vue[i]
        elif arr.vue[i] < mini:
            mini = arr.vue[i]
    return mini, maxi
