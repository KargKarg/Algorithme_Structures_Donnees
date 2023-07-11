def empiler(stack, objet: any) -> bool:
    """
    Arguments:
        - stack (instance): pile créé par la classe Pile.
        - objet (instance): élément à mettre dans la pile.

    Retours:
        - True: si l'élément est inséré.
        - False: si non, la pile est pleine

    Complexité:
        - O(1)

    Résumé:
        Fonction qui ajoute un élément à la pile.

    """
    if stack.sommet == stack.nmax-1:
        return False
    else:
        stack.vue[stack.sommet + 1] = objet
        stack.sommet += 1
        return True
