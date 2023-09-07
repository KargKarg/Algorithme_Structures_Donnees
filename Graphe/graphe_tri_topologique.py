from Graphe import graphe_lecture


def tri(path: str) -> list or bool:
    """
    Algorithme de calcul du tri topologique d'un DAG.

    Argument:
        - path (str): Chemin vers le graphe au format texte.

    Return:
        - (list or bool): La liste des sommets triées, Faux sinon.

    """
    G, _, _ = graphe_lecture.matrice_adjacence(path)

    tri_sommets = []
    cpt = 0

    while cpt <= G.shape[0]:
        cpt += 1
        for i in range(G.shape[0]):
            if i+1 not in tri_sommets:
                d_entrant_nul = True
                for j in range(G.shape[1]):
                    if G[j, i] > 0:
                        d_entrant_nul = False
                if d_entrant_nul:
                    for j in range(G.shape[0]):
                        G[i, j] = 0
                    tri_sommets.append(i+1)

    if len(tri_sommets) == G.shape[0]:
        return tri_sommets
    else:
        return False
