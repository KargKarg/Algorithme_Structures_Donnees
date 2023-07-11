def vide(stack) -> bool:
    """
    Arguments:
        - stack (instance): pile créé par la classe Pile.

    Retours:
        - True: si la pile est vide.
        - False: si non.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui teste si une pile est vide.

    """
    if stack.sommet == -1:
        return True
    else:
        return False
