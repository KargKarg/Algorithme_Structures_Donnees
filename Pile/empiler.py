def empiler(stack, objet):
    if stack.sommet == stack.nmax-1:
        return False
    else:
        stack.vue[stack.sommet + 1] = objet
        stack.sommet += 1
        return True
