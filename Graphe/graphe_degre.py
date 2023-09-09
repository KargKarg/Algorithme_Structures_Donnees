from Graphe import graphe_lecture


def calcul(path: str, oriente: bool = True) -> tuple or list:
    """
    Algorithme permettant de calculer le degré (entrant ou sortant, si graphe orienté) de chaque sommet.

    Complexité:
        - O(n^2)

    Argument:
        - path (str): Chemin vers le graphe en fichier texte.
        - oriente (bool): Vrai si le graphe est orienté, Faux sinon.

    Return:
        - degre_entrant (list): Liste des degrés entrants de chaque sommet.
        -> degre_entrant[i] = degré entrant du sommet i.

        - degre_sortant (list): Liste des degrés sortants de chaque sommet.
        -> degre_sortant[i] = degré sortant du sommet i.

        - degre (list): Liste des degrés de chaque sommet.
        -> degre[i] = degré du sommet i.
    """
    G, _, _ = graphe_lecture.matrice_adjacence(path, oriente)
    if oriente:

        degre_entrant = [0 for _ in range(G.shape[0])]
        degre_sortant = [0 for _ in range(G.shape[0])]

        for i in range(G.shape[0]):
            for j in range(G.shape[1]):
                if G[i, j] == 1:
                    degre_sortant[i] += 1
                    degre_entrant[j] += 1

        return degre_entrant, degre_sortant

    if not oriente:

        degre = [0 for _ in range(G.shape[0])]

        for i in range(G.shape[0]):
            for j in range(i+1, G.shape[1]):
                if G[i, j] == 1:
                    degre[i] += 1
                    degre[j] += 1

        return degre
