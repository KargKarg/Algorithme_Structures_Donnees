class Pile:

    def __init__(self, nmax):
        self.vue = [None for _ in range(nmax)]
        self.nmax = nmax
        self.sommet = -1
