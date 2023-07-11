def ajouter(queue, objet):
    if queue.fin == queue.nmax - 1 and queue.vue[0] is None:
        queue.fin = 0
        queue.vue[queue.fin] = objet
        return True
    elif queue.fin != queue.nmax - 1 and queue.vue[queue.fin+1] is None:
        queue.vue[queue.fin+1] = objet
        queue.fin += 1
        return True
    else:
        return False
