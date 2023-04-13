from math import *

def sommeEspece(T,nbEsp):
    sommeEsp = 0
    for i in range(nbEsp):
        sommeEsp = sommeEsp + T[i+2]
    return sommeEsp



def TestQt(Taille,n,T,Espece,nbEsp,testEspece):
    x = n%Taille
    y = n//Taille
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
    print("Trie du tableau ...")
    for i in range(Taille):
        for j in range(Taille):
            TabAux[nbCase] = [nbCase,sommeEspece(T[i][j],nbEsp)]
            nbCase = nbCase + 1
    for i in range(Taille**2):
        max = TabAux[i][1]
        for j in range(i,Taille**2):
            if TabAux[j][1] > max:
                max = TabAux[j][1]
                vartemp = j
        tmp=TabAux[i]
        TabAux[i]=TabAux[vartemp]
        TabAux[vartemp]=tmp
    testEspece = [0]*nbEsp
    n = 0
    test = TestQt(Taille,TabAux[0][0],T,Espece,nbEsp,testEspece)
    print("Cherche les solutions ...")
    while test == False :
        solution = solution + [TabAux[n][0]]
        n = n + 1
        test = TestQt(Taille,TabAux[n][0],T,Espece,nbEsp,testEspece)
    #print(TabAux)
    print(Espece)
    print(testEspece)
    return solution