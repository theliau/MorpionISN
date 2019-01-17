#Définition du tableau principal
tables = [0, 1, 2,\
          3, 4, 5,\
          6, 7, 8] #Tableaux de 9 sous-tableaux

#Définition des tableaux secondaires
#Tableaux secondaires si par exemple tableSecond[0] == 0 personne n'a joué sur cette case
#                                    tableSecond[0] == 1 le joueur 1 a joué sur cette case
#                                    tableSecond[0] == 2 le joueur 2 a joué sur cette case


def createTables():
    """
    Cette fonction crée le tableau principal.
    Le tableau principal contient les 9 tableaux secondaires.
    La fonction renvoie le tableau principal.
    """

    #Définition des 9 tableaux secondaires
    for i in range(9):
        tableSecond = [0, 0, 0,\
                       0, 0, 0,\
                       0, 0, 0]
        tables[i] = tableSecond

    #Renvoie du tableau principal contenant les 9 tableaux secondaires
    return tables

#EXEMPLE d'utilisation de la fonction:
#   tableauPrincipal = Tableaux.createTables()


def openTable(index):
    """
    Cette fonction permet de trouver le tableau voulu.
    La fonction prend un argument #index (Nombre entier entre 1 et 9 compris)
    #index est l'ID du tableau secondaire dans le tableau principal.
    La fonction renvoie le tableau secondaire voulu.
    """

    #L'index doit être compris entre 1 et 9, si ce n'est pas le cas on lève une erreur.
    if index < 1 or index > 9:
        raise Exception("L'index doit être entre 1 et 9 ! Ici il vaut : {}".format(index))
    
    return tables[index-1]

#EXEMPLE d'utilisation de la fonction:
#Si je veux le tableau secondaire numéro 1
#   openTable(1)
