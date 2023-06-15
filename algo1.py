from math import *

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

def sommeEspece(T,nbEsp):
    sommeEsp = 0
    for i in range(nbEsp):
        sommeEsp = sommeEsp + T[i+2]
    return sommeEsp

def TestQt(Taille,n,T,Espece,nbEsp,testEspece):
    x = n%Taille
    y = n//Taille
    #print("Test Espece :",testEspece ,"Espece :",Espece, T[x][y])
    for i in range(nbEsp):
        testEspece[i] = testEspece[i] + T[x][y][i+2]
    for i in range(nbEsp):
        if Espece[i] > testEspece[i]:
            return False
    return True

def algo1(T,Taille,Espece,nbEsp):
    solution = []
    TabAux = [0]*(Taille**2)
    nbCase = 0
    
    for i in range(Taille):
        for j in range(Taille):
            TabAux[nbCase] = [j*Taille+i,sommeEspece(T[i][j],nbEsp)]
            nbCase = nbCase + 1
    TabAux = trifusion(TabAux)
    
    testEspece = [0]*nbEsp
    
    n = 0
    test = TestQt(Taille,TabAux[0][0],T,Espece,nbEsp,testEspece)
    while test == False :
        solution = solution + [TabAux[n][0]]
        n = n + 1
        test = TestQt(Taille,TabAux[n][0],T,Espece,nbEsp,testEspece)
    solution = solution + [TabAux[n][0]]
    return solution