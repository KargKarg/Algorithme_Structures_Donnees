def unimodal(arr):
    variation = 0
    for i in range(arr.fin):
        if arr.vue[i] > arr.vue[i+1] and variation == 0:
            variation += 1
        elif arr.vue[i] < arr.vue[i+1] and variation > 0:
            return False
    return True
