from math import *

#Version à modifier de l'algo 1 en ne prenant pas en compte les espèces qui sont déjà protégée

def fusion(T1,T2):
    #print("les tabs",T1,T2)
    len1 = len(T1)
    len2 = len(T2)
    T3 = [0]*(len1+len2)
    if len1==1 and len2==1:
        if T1[0][1]>T2[0][1]:
            T3[0]=T1[0]
            T3[1]=T2[0]
        else:
            T3[1]=T1[0]
            T3[0]=T2[0]
        return T3
    i = 0
    j = 0
    cpt = 0
    while cpt < len1+len2:
        #print("i et len1",i,len1)
        #print("j et len2",j,len2)
        #print(T1[i][1],T2[j][1])
        if j>=len2 and i<len1:
            T3[cpt] = T1[i]
            cpt = cpt + 1
            i = i + 1
        elif i<len1 and T1[i][1]>T2[j][1]:
            T3[cpt] = T1[i]
            cpt = cpt + 1
            i = i + 1
        else:
            T3[cpt] = T2[j]
            cpt = cpt + 1
            j = j + 1
    return T3

def trifusion(T):
    long = len(T)
    if long == 1:
        return T
    else:
        mil = long//2
        T1 = [0]*mil
        T2 = [0]*(long-mil)
        for i in range(mil):
            T1[i]=T[i]
        for j in range(long-mil):
            T2[j]=T[mil+j]
        #print("Tab in trif:",T1,T2)
        return fusion(trifusion(T1),trifusion(T2))

def SecteurAExclure(i,j,Solution,Taille): #renvoie True si le secteur est déjà protégé
    for TEST in Solution:
        if TEST == j*Taille+i:
            return True
    return False

def sommeEspece(T,NonExclu):    # permet de compter seulement les espèces que l'on a pas protéger
    sommeEsp = 0
    for i in range(len(NonExclu)):
        if NonExclu[i] !=-1:
            sommeEsp = sommeEsp + T[NonExclu[i]+1]
    return sommeEsp

def TestQt(Taille,n,T,Espece,testEspece,NonExclu):
    temporaire = False
    x = n%Taille
    y = n//Taille
    for i in NonExclu:
        if i !=-1:
            #print("i=",i,NonExclu)
            #print("Test Espece :",testEspece ,"Espece :",Espece, T[x][y])
            testEspece[i-1] = testEspece[i-1] + T[x][y][i+1]
    for i in range(len(NonExclu)):
        if i !=-1:
            if Espece[i-1] < testEspece[i-1]:
                NonExclu[i-1] = -1
                temporaire = True
    return temporaire

def TestToutProteger(NonExclu):
    for i in NonExclu:
        if i !=-1:
            return False
    return True

def algo2(T,Taille,Espece,nbEsp):
    NonExclu=[0]*nbEsp
    for i in range(len(NonExclu)):
        NonExclu[i] = i+1
    solution = []
    TabAux = [0]*(Taille**2)
    testEspece = [0]*nbEsp
    
    while TestToutProteger(NonExclu) == False:
        nbCase = 0
        for i in range(Taille):
            for j in range(Taille):
                if SecteurAExclure(i,j,solution,Taille) == True:
                    ValeurSomme = 0
                else:
                    ValeurSomme = sommeEspece(T[i][j],NonExclu)
                TabAux[nbCase] = [j*Taille+i,ValeurSomme]
                nbCase = nbCase + 1
        TabAux = trifusion(TabAux)
        
        n = 0
        test = TestQt(Taille,TabAux[0][0],T,Espece,testEspece,NonExclu)
        while test == False :
            solution = solution + [TabAux[n][0]]
            n = n + 1
            test = TestQt(Taille,TabAux[n][0],T,Espece,testEspece,NonExclu)
        solution = solution + [TabAux[n][0]]
    return solution