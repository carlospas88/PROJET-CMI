import csv
#Les solutions sont passées sous forme de tableau, avec comme valeurs les zones protégée dans le cas de l'hypothèse 1, et des tableaux contenant les valeurs
#de chaque zone pour les hypothèses 2 et 3

def ecritureSolution(TabSolution,nbZone,nbSecteur):
    fichier = open(r"C:\Users\tomgi\Documents\Projet Optim\solution.txt",'w',newline='')
    solution=csv.writer(fichier,delimiter=";")
    solution.writerow(str(nbSecteur))
    solution.writerow(str(nbZone))
   
    # on regarde si on est dans le cas de l'hypothèse 1, cad une seule zone avec un entier comme première valeur du tableau et non un tableau ce qui
    #voudrait dire que l'on est dans le cas de l'hypothèse 2 ou 3 (le role de isinstance() est de vérifier si TabSol[0] est un entier, définie de base dans python)
    if nbZone == 1 and isinstance(TabSolution[0], int):
            for i in range(nbZone):
                  TabSolution[i] = str(TabSolution[i])
            solution.writerow(TabSolution)
    
    #si on n'est pas dans le cas de l'hypothèse 1, alors on est dans le cas des hypothèses 2 et 3 avec des zones
    else:
        for i in range(nbZone):
            for j in range(len(TabSolution[i])):    
                TabSolution[i][j] = str(TabSolution[i][j])

        for i in range(nbZone):
                solution.writerow(str(TabSolution[i]))