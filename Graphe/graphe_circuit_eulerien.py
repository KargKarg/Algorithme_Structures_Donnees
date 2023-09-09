from Graphe import graphe_lecture
from Graphe import graphe_transformation
from Graphe import graphe_degre
from Graphe import graphe_parcours
from Structures import file
from File import file_ajouter, file_supprimer


def eulerien(path: str) -> False or list:
    """
    Algorithme calculant le circuit Eulérien d'un graphe.

    Argument:
        - path (str): Le chemin vers le graphe au format texte.

    Return:
        - False: Si le graphe ne possède pas de circuit Eulérien.
        - circuit (list): Liste contenant les arcs successifs pour former le circuit.
            -> circuit[i]: Le i ème arc sur le circuit.
    """
    G, _, A = graphe_lecture.matrice_adjacence(path)
    q = file.File(G.shape[0])
    traites = set()
    degres_entrant, degres_sortant = graphe_degre.calcul(path)
    circuit = []

    for i in range(len(degres_sortant)):
        if degres_entrant[i] != degres_sortant[i]:
            return False

    G_T = graphe_transformation.transpose(G)
    anti_arborescence_couvrante = graphe_parcours.largeur(G_T, 1)

    arcs_marques = {(i+1, anti_arborescence_couvrante[i]) for i in range(len(anti_arborescence_couvrante)) if anti_arborescence_couvrante[i] is not None}
    restants_marques = arcs_marques.copy()

    file_ajouter.ajouter(q, 1)

    while traites != A:

        sommet = file_supprimer.supprimer(q)

        for j in range(G.shape[1]):
            if G[sommet-1, j] == 1 and (sommet, j+1) not in arcs_marques and (sommet, j+1) in A - traites:
                traites.add((sommet, j+1))
                file_ajouter.ajouter(q, j+1)
                circuit.append((sommet, j+1))
                break
            elif G[sommet-1, j] == 1 and (sommet, j+1) in A - traites and not any(k == sommet for (k, z) in A - traites - restants_marques):
                traites.add((sommet, j + 1))
                file_ajouter.ajouter(q, j + 1)
                restants_marques -= {(sommet, j+1)}
                circuit.append((sommet, j + 1))
                break

    return circuit
