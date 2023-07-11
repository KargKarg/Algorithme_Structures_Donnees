def supprimer(queue):
    if queue.tete == queue.nmax:
        queue.tete = 0
    objet = queue.vue[queue.tete]
    queue.vue[queue.tete] = None
    queue.tete += 1
    return objet
