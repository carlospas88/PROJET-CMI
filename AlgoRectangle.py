#algo rectange


def TestRectangle(coord1,coord2,TabDonnee,nbEsp,Taille):
    TabEspRectangle = [0]*nbEsp
    x1 = coord1%Taille
    y1 = coord1//Taille
    x2 = coord2%Taille
    y2 = coord2//Taille
    xmin = min(x1,x2)
    xmax = max(x1,x2)
    ymin = min(y1,y2)
    ymax = max(y1,y2)
    nbSecteurs = (xmax-xmin+1)*(ymax-ymin+1)
    for x in range(xmin,xmax+1):
        for y in range(ymin,ymax+1):
            if TabDonnee[x][y][1] == 1:
                return False,nbSecteurs
            for i in range(nbEsp):
                TabEspRectangle[i] = TabEspRectangle[i] + TabDonnee[x][y][i+2]
    for TEST in TabEspRectangle:
        if TEST != 0:
            return (TabEspRectangle,nbSecteurs)
    return False,nbSecteurs

def AlgoRectangle(TabDonnee,Taille,Espece,nbEsp,nbZones):
    #première étape, faire une liste de tout les rectangles valides et faire la somme pour chaque espece aussi
    #Ces rectangles seront mis dans le tableau ListeRectangle avec le format suivant [coordonée de départ, [coordonnée de fin, quantité Esp1,... quantité dernière espèce]]
    ListeRectangle = []
    positionListe = 0
    for coord1 in range(Taille*Taille):
        for coord2 in range(coord1,Taille*Taille):
            (TestPossible,nbSecteurs) = TestRectangle(coord1,coord2,TabDonnee,nbEsp,Taille)
            if TestPossible != False:
                ListeRectangle = ListeRectangle + [[coord1,coord2,nbSecteurs,[]]]
                for i in TestPossible:
                    ListeRectangle[positionListe][3] = ListeRectangle[positionListe][3] + [i]
                positionListe = positionListe +1
    
    # Maintenant que l'on a une liste de tout les rectangles possibles on cherche une solution possible
    ListeRectanglesSolution = []
    ListeRectanglesPossibles = []
    
    if nbZones == 2:
        #11/20 + 9 /20
        #On cherche Tout les Rectangles de 11/20
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(11/20):
                    TEST = False
                cpt = cpt +1
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 11/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]

        #On cherche Tout les Rectangles de 9/20 mainteant en vérifiant qu'il ne se superpose pas avec l'autre rectangle
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(9/20):
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 9/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
    
    if nbZones == 3:
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/2):
                    TEST = False
                cpt = cpt +1
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 11/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]

        #On cherche Tout les Rectangles de 9/20 mainteant en vérifiant qu'il ne se superpose pas avec l'autre rectangle
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/3):
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 9/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/6):
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 9/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
    
    if nbZones == 4:
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(9/20):    ###############################
                    TEST = False
                cpt = cpt +1
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 11/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(5/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(4/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(2/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
    
    if nbZones == 5:
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/3):    ###############################
                    TEST = False
                cpt = cpt +1
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 11/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/4):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/5):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/6):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
    
    if nbZones == 6:
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(3/10):    ###############################
                    TEST = False
                cpt = cpt +1
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 11/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/4):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/5):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x01,x02)
                        xmax = max(x01,x02)
                        ymin = min(y01,y02)
                        ymax = max(y01,y02)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(3/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
    
    if nbZones == 7:
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/4):    ###############################
                    TEST = False
                cpt = cpt +1
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        #On cherche Le plus petit 11/20
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/5):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/5):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(3/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/10):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]
        #######    ###############################
        ListeRectanglesPossibles = []
        for Rectangle in ListeRectangle:
            TEST = True
            cpt = 0
            while TEST != False and cpt<nbEsp:
                if Rectangle[3][cpt]<Espece[cpt]*(1/20):    ###############################
                    TEST = False
                cpt = cpt +1
                #on vérifie la superposition
                for RectSuperpose in ListeRectanglesSolution:
                        x1 = RectSuperpose[0]%Taille
                        y1 = RectSuperpose[0]//Taille
                        x2 = RectSuperpose[1]%Taille
                        y2 = RectSuperpose[1]//Taille
                        x01 = Rectangle[0]%Taille
                        y01 = Rectangle[0]//Taille
                        x02 = Rectangle[1]%Taille
                        y02 = Rectangle[1]//Taille
                        xmin = min(x1,x2)
                        xmax = max(x1,x2)
                        ymin = min(y1,y2)
                        ymax = max(y1,y2)
                        xmin2 = min(x01,x02)
                        xmax2 = max(x01,x02)
                        ymin2 = min(y01,y02)
                        ymax2 = max(y01,y02)
                        if (xmin-1 <= x01 and x01 <= xmax+1) or (xmin-1 <= x02 and x02 <= xmax+1) or (xmin2-1 <= x1 and x1 <= xmax2+1) or (xmin2-1 <= x2 and x2 <= xmax2+1):
                            if (ymin-1 <= y01 and y01 <= ymax+1) or (ymin-1 <= y02 and y02 <= ymax+1) or (ymin2-1 <= y1 and y1 <= ymax2+1) or (ymin2-1 <= y2 and y2 <= ymax2+1) :
                                TEST = False
            if TEST == True:
                ListeRectanglesPossibles = ListeRectanglesPossibles + [Rectangle]
        RectangleRetenu = []
        nbSecteurMin = Taille*Taille
        for RecherchePlusPetit in ListeRectanglesPossibles:
            if RecherchePlusPetit[2]<nbSecteurMin:
                nbSecteurMin = RecherchePlusPetit[2]
                RectangleRetenu = RecherchePlusPetit
        if len(RectangleRetenu) == 0:
            return False
        ListeRectanglesSolution = ListeRectanglesSolution + [RectangleRetenu]

    solution = [[]]*nbZones
    for i in range(nbZones):
        coord1 = ListeRectanglesSolution[i][0]
        coord2 = ListeRectanglesSolution[i][1]
        x1 = coord1%Taille
        y1 = coord1//Taille
        x2 = coord2%Taille
        y2 = coord2//Taille
        xmin = min(x1,x2)
        xmax = max(x1,x2)
        ymin = min(y1,y2)
        ymax = max(y1,y2)
        for x in range(xmin,xmax+1):
            for y in range(ymin,ymax+1):
                solution[i] = solution[i] + [y*Taille+x]
    return solution