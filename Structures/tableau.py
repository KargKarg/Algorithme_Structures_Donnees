class Tableau:
    """
    Enregistrement Tableau {
        nmax: entier;
        vue: Tableau;
        fin: entier
    }

    nmax (int): nombre de case attribué au tableau.
    vue (list): représentation du tableau.
    fin (int): l'indice du dernier élément du tableau.

    """
    def __init__(self, nmax):
        self.nmax = nmax
        self.vue = [None for _ in range(self.nmax)]
        self.fin = -1
