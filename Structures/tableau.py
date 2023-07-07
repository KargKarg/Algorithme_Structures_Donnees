class Tableau:

    def __init__(self, nmax):
        self.nmax = nmax
        self.vue = [None for _ in range(self.nmax)]
        self.fin = -1
