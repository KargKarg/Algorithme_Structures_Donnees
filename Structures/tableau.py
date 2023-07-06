class Tableau:

    vue = []
    fin = -1

    def __init__(self, nmax):
        self.nmax = nmax
        Tableau.vue = [None for _ in range(self.nmax)]
        Tableau.fin = -1
