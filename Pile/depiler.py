from pile_vide import vide


def depiler(stack):
    if not vide(stack):
        element = stack.vue[stack.sommet]
        stack.vue[stack.sommet] = None
        stack.sommet -= 1
        return element
    else:
        return False
