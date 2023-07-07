class File:

    def __init__(self, nmax):
        self.nmax = nmax
        self.vue = [None for _ in range(nmax)]
        self.tete = 0
        self.fin = -1
