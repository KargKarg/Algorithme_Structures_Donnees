def ajouter(queue, objet: any) -> bool:
    """
    Arguments:
        - queue (instance): file créé par la classe File.
        - objet (any): élément de n'importe quel type.

    Retours:
        - True: si l'élément est inséré.
        - Faux: si non, car file pleine.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui ajoute un élément dans la file.

    """
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
