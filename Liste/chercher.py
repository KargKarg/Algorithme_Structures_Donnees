from Structures import listech


L = listech.Liste()

def chercher(liste, objet):
    cpt = 0
    while len(liste.vue[cpt:]) != 0 and liste.vue[cpt] != objet:
        cpt += 1
    if len(liste.vue[cpt:]) == 0:
        return None
    else:
        return cpt
