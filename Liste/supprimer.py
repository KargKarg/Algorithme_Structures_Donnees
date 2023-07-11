from chercher import chercher


def supprimer(liste, objet):
    indice = chercher(liste, objet)
    if indice is not None:
        g = liste.vue[:indice]
        d = liste.vue[indice+1:]
        liste.vue = g + d
        return True
    else:
        return False
