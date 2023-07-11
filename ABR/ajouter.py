from Structures import arbre


def ajouter(noeud, entier):
    if entier <= noeud.valeur and noeud.gauche is None:
        gauche = arbre.ABR(entier)
        noeud.gauche = gauche
    elif entier <= noeud.valeur:
        ajouter(noeud.gauche, entier)
    elif entier > noeud.valeur and noeud.droite is None:
        droite = arbre.ABR(entier)
        noeud.droite = droite
    else:
        ajouter(noeud.droite, entier)
