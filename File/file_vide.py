def vide(queue) -> bool:
    """
    Arguments:
        - queue (instance): file créé par la classe File.

    Retours:
        - True: si la file est vide.
        - Faux: si non.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui teste si la file est vide.

    """
    if queue.vue[queue.tete] is None:
        return True
    else:
        return False
