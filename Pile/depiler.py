def depiler(stack):
    element = stack.vue[stack.sommet]
    stack.vue[stack.sommet] = None
    stack.sommet -= 1
    return element
