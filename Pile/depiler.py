from Pile import pile_vide


def depiler(stack) -> int:
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
    if not pile_vide.vide(stack):
        element = stack.vue[stack.sommet]
        stack.vue[stack.sommet] = None
        stack.sommet -= 1
        return element
