def empiler(stack, objet):
    stack.vue[stack.sommet+1] = objet
    stack.sommet += 1
