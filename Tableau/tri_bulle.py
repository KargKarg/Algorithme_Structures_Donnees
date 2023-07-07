def tri_bulle(arr):
    for i in range(arr.fin+1):
        switch = False
        for j in range(arr.fin, i, -1):
            if arr.vue[j-1] > arr.vue[j]:
                flag = arr.vue[j-1]
                arr.vue[j-1] = arr.vue[j]
                arr.vue[j] = flag
                switch = True
        if not switch:
            break
