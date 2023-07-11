class Pile:
    """
    Enregistrement Pile {
        nmax: entier;
        vue: Tableau;
        sommet: entier
    }

    nmax (int): nombre de case attribué à la pile.
    vue (list): tableau représentant la pile.
    sommet (int): l'indice de l'élément prioritaire.

    """
    def __init__(self, nmax):
        self.vue = [None for _ in range(nmax)]
        self.nmax = nmax
        self.sommet = -1
