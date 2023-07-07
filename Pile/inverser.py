from Structures import pile
from empiler import empiler
from depiler import depiler
from pile_vide import vide


def inverser(stack):
    stack_inv = pile.Pile(stack.nmax)
    while not vide(stack):
        empiler(stack_inv, depiler(stack))
    stack.vue = stack_inv.vue
    stack.sommet = stack_inv.sommet
