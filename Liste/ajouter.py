def ajouter(liste, objet: any) -> bool:
    """
    Arguments:
        - liste (instance): liste chaînée créée par la classe Liste.

    Retours:
        - True: si l'élément est inséré.
        - False: si non.

    Complexité:
        - O(1)

    Résumé:
        Fonction qui ajoute un élément à la liste chaînée.

    """
    liste.vue = [objet] + liste.vue
    return True
