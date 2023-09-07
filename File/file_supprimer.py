def supprimer(queue) -> int:
    """
    Arguments:
        - queue (instance): file créé par la classe File.

    Retours:
        - objet (any): l'élément prioritaire de la file.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui renvoie l'élément prioritaire de la file en le supprimant.

    """
    if queue.tete == queue.nmax-1:
        objet = queue.vue[queue.tete]
        queue.vue[queue.tete] = None
        queue.tete = 0
        return objet
    objet = queue.vue[queue.tete]
    queue.vue[queue.tete] = None
    queue.tete += 1
    return objet
