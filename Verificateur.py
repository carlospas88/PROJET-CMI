def doublons(T):       # Permet de vérifier si un secteur n'a pas été protéger plusieur fois
    for i in range(len(T)):
        for j in range(i+1,len(T)):
            if T[i] == T[j]:
                return True
    return False

# Le vérificateur prend en paramètre :
# - Le tableau que l'on a réalisé grace au lecteur qui correspond le nombre de poisson par case (TableauLectureCsv)
# - Le tableau de solution que l'on veut vérifier qui est sont la forme [16,24,...,13] pour le cas 1 et sous la forme
#   [[16,24,...,13],[16,24,...,13],...,[16,24,...,13]] pour les cas 2 et 3 chaque tableau correspondant à une zone
# - Le nombre de zone qui est 1 dans le cas 1
# - Le nombre total de secteur que l'on a protégé
# - Le cas (1 2 ou 3)
# - Le tableau avec les quantité minimun à protéger pour chaque espèce réaliser dans le lecteur (espece)
# - La longeur/largeur (même nombre) du fichier que l'on regarde
# - Un booléen (InfoErreur) qui quand il vaut True permet d'afficher précisément les raisons pour lequelles la solution est incorrecte
#   et qui permet de ne pas s'arreter à la première erreur que l'on rencontre


def verificateur(TableauLectureCsv,TabSolution,nbZone,nbSecteur,cas,espece,Taille,InfoErreur):
    #on commence par vérifier si tous les paramètres sont valides entre eux
    if cas == 1:
        cas2 = True
    else:
        cas2 = False
    tailleSol = len(TabSolution)
    TestCas = True
    erreur = False
    for i in range(tailleSol):
        TestCas1 = isinstance(TabSolution[0], int)
        if TestCas1 == False:
            TestCas = False
    if TestCas != cas2:
        if InfoErreur == True:
            print("Le tableau de solution n'est pas dans le bon formet par rapport au cas choisi")
            erreur = True
        else:
            return False
    if cas2 == True:
        if tailleSol != nbSecteur:
            if InfoErreur == True:
                print("Le nombre de secteur ne correspond pas à celui dans le tableau de solution")
                erreur = True
            else:
                return False
    else:
        cpt = 0
        for i in range(len(TabSolution)):
            cpt = cpt + len(TabSolution[i])
        if tailleSol != nbZone:
            if InfoErreur == True:
                print("Le nombre de zone ne correspond pas à celui dans le tableau de solution")
                erreur = True
            else:
                return False
        if cpt != nbSecteur:
            if InfoErreur == True:
                print("Le nombre de secteur ne correspond pas à celui dans le tableau de solution")
                erreur = True
            else:
                return False

    if erreur == True and InfoErreur == True:
        # si les paramètres en entrée sont incorrecte alors on ne pourra pas lire le tableau correctement, on s'arrete
        # donc ici pour eviter une erreur du programme
        print("Erreur, impossible de continuer à cause de l'une des erreurs ci dessus")
        return
    
    # si les paramètres sont conforme on peut continuer la vérifisation , on vas commencer par la vérification si on est dans le cas 1

    # pour le cas 1, on doit vérifier si : aucune case de Terre n'a été protégée et si le nombre de poisson protégé est correct 

    nbEsp = len(espece)
    testEspece = [0] * nbEsp
    if cas == 1:
        if doublons(TabSolution) == True:
            if InfoErreur == True:
                print("Il a une zone protégée deux fois")
            else:
                return False
    
        
        for case in TabSolution:
            y = case//Taille
            x = case%Taille
            if TableauLectureCsv[x][y][0] != case:
                if InfoErreur == True :
                    print("Erreur, problème de coordonée impossible de continuer, x =",x,",y=",y,",case=",case,",TableauLectureCsv[x][y][0]=",TableauLectureCsv[x][y][0])
                else:
                    return False
            if TableauLectureCsv[x][y][1] == 1:
                if InfoErreur == True:
                    print("La case ",case," a été protégée alors qu'il s'agit d'une case de Terre")
                else:
                    return False
            for i in range(nbEsp):
                testEspece[i] = testEspece[i] + TableauLectureCsv[x][y][i+2]
        for j in range(nbEsp):
            if testEspece[j]<espece[j]:
                if InfoErreur == True:
                    print("La quantité protégée pour l'espèce ",j," n'est pas suffisante")
                else:
                    return False
        if InfoErreur == True:
            print("Si aucun message d'erreur n'est apparu alors la solution est correcte")
        
        return True

    # pour le cas 2, on véfifie les mêmes conditions mais on doit vérifier en plus que chaque zone est rectangle :
    # pour cela on prend les 2 coins en haut à gauche et en bas à droite de la zone, soit le secteur de plus petit indice et celui de plus grand et on vérifie
    # que l'on a bien toute les zones entre xa et xb pour tout x entre xa et xb et ya yb aussi

    # TabSuperposition va nous permetre de vérifier que les zones ne se superposent pas, on va y mettre les coordonnée des coins de chaque zone lorsque
    # l'on vérifie les zones individuellement

    if cas == 2:
        TabSuperposition = [0]* len(TabSolution)
        NumZone = 0

        #On regarde les zones une par une
        for TabZone in range(TabSolution):

            #on vérifie qu'il n'y a pas de doublons à l'intérieur de la zone
            if doublons(TabZone) == True:
                if InfoErreur == True:
                    print("Il a une zone protégée deux fois")
                else:
                    return False

            #on cherche le min et le max pour avoir les deux coins de la zone
            min = TabZone[0] 
            max = 0
            for j in range(TabZone):
                if j<min:
                    min = j
                elif j>max:
                    max = j
            x1 = min%Taille
            x2 = max%Taille
            y1 = min//Taille
            y2 = max//Taille

            TabSuperposition[NumZone] = [x1,x2,y1,y2]
            # on regarde si la taille du tableau de la zone correspond à l'aire pour savoir si on a protéger le bon nombre de zone
            if len(TabZone) != (x2-x1+1)*(y2-y1+1):
                if InfoErreur == True:
                    print("Une des zones ne protège pas le bon nombre de secteur (différent de L*l)")
                else:
                    return False
        
            #on parcourt ensuite toute la zone afin de chercher si il y a des zones de terre ou si il manque des cases que l'on a pas protéger ou des cases en trop
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if TableauLectureCsv[x][y][1] == 1:
                        if InfoErreur == True:
                            print("Le secteur",y*Taille+x,"appartient à la zone",NumZone,"alors que c'est un secteur de terre")
                        else:
                            return False
                    
            for h in range(len(TabZone)):
                x = TabZone[h]%Taille
                y = TabZone[h]//Taille
                if x<x1 or x>x2 or y<y1 or y>y2:
                    if InfoErreur == True:
                        print("Un secteur en dehors de la zone",NumZone,"a été protégé")
                    else:
                        return False

        NumZone = NumZone + 1
    # si dans une zone il n'y a pas de doublons, il y a le bon nombre de secteur protégé et ils appartiennent tous à la zone alors on est certain que la zone
    # est correcte, si il y a un doublons dans une autre zone, alors soit il sera en dehors de la zone, soit deux zones sont superpose (à vérifier après)

    #on vérifie que 2 zones ne sont pas superposée, pour cela pour chaque paire de zone on regarde l'intersection entre [x1a,x1b] et [x2a,x2b] ainsi que celle entre
    #[y1a,y1b] et [y2a,y2b], si les deux intersections ne sont pas vides alors les zones se superposent

        for i in range(NumZone):
            for j in range(i,NumZone):
                1





# pour vérifier la superposition du cas 3, vérifier la connexité de deux zones , si il y a une zone, se superposent,
# sinon si deux zones, bon car on vérifie chaque zone individuellement avant ?