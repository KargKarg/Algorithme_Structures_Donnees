class File:
    """
    Enregistrement File {
        nmax: entier;
        vue: Tableau;
        tete: entier;
        fin: entier
    }

    nmax (int): nombre de case attribué à la file.
    vue (list): tableau représentant la file.
    tete (int): l'indice de l'élément prioritaire.
    fin (int): l'indice du dernier élément de la file.

    """
    def __init__(self, nmax):
        self.nmax = nmax
        self.vue = [None for _ in range(nmax)]
        self.tete = 0
        self.fin = -1
