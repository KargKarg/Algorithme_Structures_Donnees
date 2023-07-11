from pile_vide import vide


def depiler(stack) -> None:
    """
    Arguments:
        - stack (instance): pile créé par la classe Pile.

    Retours:
        - (any): élément dans la pile.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui renvoie l'élément prioritaire de la pile, None si elle est vide.

    """
    if not vide(stack):
        element = stack.vue[stack.sommet]
        stack.vue[stack.sommet] = None
        stack.sommet -= 1
        return element
    else:
        return None
