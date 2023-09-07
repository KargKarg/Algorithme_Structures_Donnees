from Graphe import graphe_lecture


def dag(path: str) -> bool:
    """
    Algorithme de calcul d'un DAG.

    Argument:
        - path (str): Chemin vers le graphe au format texte.

    Return:
        - (bool): Vrai si c'est un DAG, Faux sinon.

    """
    G, _, _ = graphe_lecture.matrice_adjacence(path)

    ban = set()
    cpt = 0

    while cpt <= G.shape[0]:
        cpt += 1
        for i in range(G.shape[0]):
            if i+1 not in ban:
                d_entrant_nul = True
                for j in range(G.shape[1]):
                    if G[j, i] > 0:
                        d_entrant_nul = False
                if d_entrant_nul:
                    for j in range(G.shape[0]):
                        G[i, j] = 0
                    ban.add(i+1)

    if len(ban) == G.shape[0]:
        return True
    else:
        return False

print(dag('graphe.txt'))