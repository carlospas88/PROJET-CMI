#Tab correpond au Tableau créé à partir du csv qui contient les informations, TabSolution est le tableau de solution que l'on veut vérifier
#cas correspond au cas dans lequel on se trouve 1 , 2 ou 3, entrer True pour le cas 1, False pour 2 et 3
#espece correspond au tableau contenant les quantitées à protéger

def verificateur(Tab,TabSolution,nbZone,nbSecteur,cas,espece,Taille):
    #on commence par vérifier si tous les paramètres sont valides entre eux
    tailleSol = len(TabSolution)
    TestCas = True
    erreur = False
    for i in range(tailleSol):
        TestCas1 = isinstance(TabSolution[0], int)
        if TestCas1 == False:
            TestCas = False
    if TestCas != cas:
        print("Le tableau de solution n'est pas dans le bon formet par rapport au cas choisi")
        erreur = True
    if cas == True:
        if tailleSol != nbSecteur:
            print("Le nombre de secteur ne correspond pas à celui dans le tableau de solution")
            erreur = True
    else:
        cpt = 0
        for i in range(len(TabSolution)):
            cpt = cpt + len(TabSolution[i])
        if tailleSol != nbZone:
            print("Le nombre de zone ne correspond pas à celui dans le tableau de solution")
            erreur = True
        if cpt != nbSecteur:
            print("Le nombre de secteur ne correspond pas à celui dans le tableau de solution")
            erreur = True

    if erreur == True:
        #si les paramètres en entrée sont incorrecte alors on ne pourra pas lire le tableau correctement, on s'arrete donc ici pour eviter une erreur du programme
        print("Erreur, impossible de continuer à cause de l'une des erreurs ci dessus")
        return
    
    # si les paramètres sont conforme on peut continuer la vérifisation , on vas commencer par la vérification si on est dans le cas 1

    #pour le cas 1, on doit vérifier si : aucune case de Terre n'a été protégée et si le nombre de poisson protégé est correct 
    nbEsp = len(espece)
    testEspece = [0] * nbEsp
    if cas == True:
        for case in TabSolution:
            y = case//Taille
            x = case%Taille
            if Tab[x][y][0] != case:
                print("Erreur, problème de coordonée impossible de continuer, x =",x,",y=",y,",case=",case,",Tab[x][y][0]=",Tab[x][y][0])
                return
            if Tab[x][y][1] == 1:
                print("La case ",case," a été protégée alors qu'il s'agit d'une case de Terre")
            for i in range(nbEsp):
                testEspece[i] = testEspece[i] + Tab[x][y][i+2]
        for j in range(nbEsp):
            if testEspece[j]<espece[j]:
                print("La quantité protégée pour l'espèce ",j," n'est pas suffisante")
        print("Si aucun message d'erreur n'est apparu alors la solution est correcte")


    # pour le cas 2, on véfifie les mêmes conditions mais on doit vérifier en plus que chaque zone est rectangle :
    # pour cela on prend les 2 coins en haut à gauche et en bas à droite de la zone, soit le secteur de plus petit indice et celui de plus grand et on vérifie
    # que l'on a bien toute les zones entre xa et xb pour tout x entre xa et xb
