import os
from bibimages import *
import csv  
from algo1 import *
from EcritureSolution import *
from Verificateur import *
from lecteur import *
from Affichage import *


rep = os.getcwd()  #permet d'obtenir l'adresse du repertoire dans lequel on se trouve, par ex ...\ProjetOptim
rep = rep + '\smalldata' #rep prend comme valeur l'adresse du dossier smalldata
ListeFichier = os.listdir(rep)  #permet de créer un tableau avec le nom de tous les fichiers qui se trouvent dans le dossier smalldata
#adresse = rep + '\\' + ListeFichier[0] #permet d'obtenir l'adresse du premier fichier dans smalldata, on peut ensuite faire une boucle pour tout lire en changeant l'indice

def VerifSolutionPossible(Taille,nbEsp,Espece,T):
    testEspece = [0]*nbEsp
    for x in range(Taille):
        for y in range(Taille):
            for i in range(nbEsp):
                testEspece[i] = testEspece[i] + T[x][y][i+2]
    for i in range(nbEsp):
        if Espece[i] > testEspece[i]:
            return False
    return True

def TestAll(NumAlgo,erreur):
    for TEST in range(342):
        adresse = rep + '\\' + ListeFichier[TEST]
        file = open(adresse,'r')
        if erreur == "True":
            print("Lecture de :",adresse)
        (Taille,T,espece,nbEsp) = readfile(file)
        if VerifSolutionPossible(Taille,nbEsp,espece,T) == True:
            if NumAlgo == 1:
                Solution = algo1(T,Taille,espece,nbEsp)
            verif = verificateur(T,Solution,1,len(Solution),1,espece,Taille,False)
            if verif == False and erreur != "True":
                print("Erreur",adresse)
        else:
            print("Impossible",adresse)

def TestSeul(NumAlgo,nom,apercu):
    adresse = rep + '\\' + nom
    file = open(adresse,'r')
    (Taille,T,espece,nbEsp) = readfile(file)
    if VerifSolutionPossible(Taille,nbEsp,espece,T) == True:
        if NumAlgo == 1:
            Solution = algo1(T,Taille,espece,nbEsp)
        verificateur(T,Solution,1,len(Solution),1,espece,Taille,True)
        if apercu =="True":
            img = nouvelleImage(Taille,Taille)
            afficheApercu(Taille,T,img)
            afficheApercuFinal(Taille,Solution,img)
        print("La solution est :\n",Solution)
        print("Avec",len(Solution),"cases protégée")
    else:
        print("Il est impossible d'atteindre l'objectif de protection pour l'une des espèce")

TypeTest = input("Entrer le type de test, 'Seul' ou 'All': ")
NumAlgo = int(input("Entrer le numéro de l'algorithme : "))
if TypeTest == "All":
    testEr = input("Entrer True pour afficher tous les noms, False pour afficher seulement ceux qui posent problème : ")
    TestAll(NumAlgo,testEr)
else:
    nom = input("Entrer le nom du fichier sous le format 'archipel_2_10_10_2.txt' par exemple : ")
    apercu = input("Entrer 'True' pour afficher une image des zones protégées : ")
    TestSeul(NumAlgo,nom,apercu)



#343 fichier à tester

# le secteur de coordonnées (x, y) a pour indice y ∗ Taille + x

# Le secteur d’indice i a pour coordonnées (i mod(Taille),⌊i/Taille⌋)