#Définition du tableau principal
tables = [0, 1, 2,\
          3, 4, 5,\
          6, 7, 8] #Tableaux de 9 sous-tableaux

#Définition des tableaux secondaires
#Tableaux secondaires si par exemple tableSecond[0] == 0 personne n'a joué sur cette case
#                                    tableSecond[0] == 1 le joueur 1 a joué sur cette case
#                                    tableSecond[0] == 2 le joueur 2 a joué sur cette case
def createAllSecondariesTables():
    for i in range(9):
        tableSecond = [0, 0, 0,\
                       0, 0, 0,\
                       0, 0, 0]
        tables[i] = tableSecond

createAllSecondariesTables()
print(tables)
