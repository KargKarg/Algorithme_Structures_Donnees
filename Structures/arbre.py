class ABR:
    """
    Enregistrement ABR{
        valeur: entier;
        gauche: ABR;
        droite: ABR
    }

    Permet de créer un arbre respectant les conditions d'ABR.

    valeur (int): la valeur enregistrée dans le noeud.
    gauche (objet): sous-arbre de gauche du noeud considéré.
    droite (objet): sous-arbre de droite du noeud considéré.

    """
    def __init__(self, entier):
        self.valeur = entier
        self.gauche = None
        self.droite = None
