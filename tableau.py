import math
import random


class Tableau:

    tableau = []
    fin = -1

    def __init__(self, nmax):
        self.nmax = nmax
        Tableau.tableau = [None for _ in range(self.nmax)]
        Tableau.fin = -1

    @staticmethod
    def inserer(entier):
        Tableau.tableau[Tableau.fin+1] = entier
        Tableau.fin += 1

    @staticmethod
    def appartient(entier):
        for i in range(Tableau.fin+1):
            if Tableau.tableau[i] == entier:
                return True
        return False

    @staticmethod
    def min_et_max():
        mini = Tableau.tableau[0]
        maxi = Tableau.tableau[0]
        for i in range(Tableau.fin+1):
            if Tableau.tableau[i] > maxi:
                maxi = Tableau.tableau[i]
            elif Tableau.tableau[i] < mini:
                mini = Tableau.tableau[i]
        return mini, maxi

    @staticmethod
    def supprimer(entier):
        for i in range(Tableau.fin+1):
            if Tableau.tableau[i] == entier:
                for j in range(i+1, Tableau.fin+2):
                    Tableau.tableau[j-1] = Tableau.tableau[j]
                Tableau.fin -= 1
                break

    @staticmethod
    def sous_somme(g, d):
        sous_somme = 0
        for i in range(g, d+1):
            sous_somme += Tableau.tableau[i]
        return sous_somme

    @staticmethod
    def sous_somme_max():
        maxi = Tableau.tableau[Tableau.fin]
        max_g, max_d = 0, 0

        for g in range(Tableau.fin+1):
            for d in range(g+1, Tableau.fin+1):
                sous_somme = Tableau.sous_somme(g, d)
                if sous_somme > maxi:
                    maxi = sous_somme
                    max_g, max_d = g, d

        return maxi, max_g, max_d

    @staticmethod
    def unimodal():
        variation = 0
        for i in range(Tableau.fin):
            if Tableau.tableau[i] > Tableau.tableau[i+1] and variation == 0:
                variation += 1
            elif Tableau.tableau[i] < Tableau.tableau[i+1] and variation > 0:
                return False
        return True

    @staticmethod
    def maximum_unimodal():
        g = 0
        d = Tableau.fin
        m = math.ceil((g+d)/2)

        while m != d and m != g:
            if Tableau.tableau[m] < Tableau.tableau[m+1]:
                g = m
                m = math.ceil((g+d)/2)
            else:
                d = m
                m = math.ceil((g+d)/2)

        return Tableau.tableau[m]

    def sans_doublons(self):

        sd_tableau = [None for _ in range(self.nmax)]
        sd_fin = -1

        for i in range(Tableau.fin+1):
            contenu = False
            for j in range(i+1, Tableau.fin+1):
                if Tableau.tableau[i] == Tableau.tableau[j]:
                    contenu = True
            if not contenu:
                sd_tableau[sd_fin+1] = Tableau.tableau[i]
                sd_fin += 1

        Tableau.tableau = sd_tableau
        Tableau.fin = sd_fin


tableau = Tableau(40)
tableau.inserer(-10)

for _ in range(35):
    tableau.inserer(random.randint(-100, 100))

print(tableau.tableau)





