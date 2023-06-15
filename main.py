import os
from bibimages import *
import csv  
from algo1 import *
from algo2 import *
from EcritureSolution import *
from Verificateur import *
from lecteur import *
from Affichage import *
from AlgoRectangle import *
import time
from Minorant import *



rep = os.getcwd()  #permet d'obtenir l'adresse du repertoire dans lequel on se trouve, par ex ...\ProjetOptim
rep = rep + '\smalldata' #rep prend comme valeur l'adresse du dossier smalldata
ListeFichier = os.listdir(rep)  #permet de créer un tableau avec le nom de tous les fichiers qui se trouvent dans le dossier smalldata


# vérif solution permet de vérifier si il est possible d'obtenir une solution car pour certain fichiers (3), il y a au moins une
# espèce qui n'est pas présente en quantité suffisante.
# il est nécessaire de le faire dès le début car sinon cela peut provoquer des bugs dans l'algorithme

def VerifSolutionPossible(Taille,nbEsp,Espece,TableauLecture):
    testEspece = [0]*nbEsp
    for x in range(Taille):
        for y in range(Taille):
            for i in range(nbEsp):
                testEspece[i] = testEspece[i] + TableauLecture[x][y][i+2]
    for i in range(nbEsp):
        if Espece[i] > testEspece[i]:
            return False
    return True

# TestAll permet de tester les 343 fichier avec un algorithme afin de savoir si il y en a qui posent problème.
# NumAlgo correspond au numéro de l'algorithme, et erreur et un booléen qui permet de dire si l'on veut afficher le nom des fichiers
# que l'on test afin de savoir si il y a un bug quel fichier le provoque (on ne l'utilisera pas en général)
# Lorsque erreur est égale à False alors le programme renvoie le nom des fichier qui posent problèmes uniquement en indiquant
# "impossible" si il n'y a pas de solution (on utilise Verif Solution) et
# "erreur" si il y a une erreur dans la solution (on utilise le vérificateur)

def TestAll(NumAlgo,erreur,k):
    if NumAlgo == 3:
        Fichier10 = [[7,13],[30,36],[53,57],[76,82],[99,105],[122,128],[154,151],[168,174],[191,197],[214,220],[237,243],[260,266],[283,289],[306,312],[329,335]]
        Fichier30 = [[14,20],[37,43]]
        for TabTEST in Fichier30:
            for TEST in range(TabTEST[0],TabTEST[1]+1):
                adresse = rep + '\\' + ListeFichier[TEST]
                file = open(adresse,'r')
                if erreur == "True":
                    print(TEST,"Lecture de :",adresse)
                (Taille,TableauLecture,espece,nbEsp) = readfile(file)
                if VerifSolutionPossible(Taille,nbEsp,espece,TableauLecture) == True:
                    debut = time.time()
                    Solution = AlgoRectangle(TableauLecture,Taille,espece,nbEsp,k)
                    temps = time.time() - debut
                    minorant = Minorant(Taille,nbEsp,espece,TableauLecture)
                    secteurs = 0
                    if Solution == False:
                        verif = -1
                    else:
                        verif = verificateur(TableauLecture,Solution,k,len(Solution),2,espece,Taille,False)
                        for sol in Solution:
                            secteurs = secteurs + len(sol)
                    if verif == False:
                        print(TEST,"Erreur",adresse)
                    if verif == -1:
                        print(ListeFichier[TEST],";",minorant,";",temps,";","Pas De Solution")
                    if verif !=-1 and verif != False:
                        print(ListeFichier[TEST],";",minorant,";",temps,";",secteurs)
                else:
                    print(ListeFichier[TEST],";","Impossible")
    else:   
        for TEST in range(342):
            adresse = rep + '\\' + ListeFichier[TEST]
            file = open(adresse,'r')
            if erreur == "True":
                print(TEST,"Lecture de :",adresse)
            (Taille,TableauLecture,espece,nbEsp) = readfile(file)
            if VerifSolutionPossible(Taille,nbEsp,espece,TableauLecture) == True:
                if NumAlgo == 1:
                    debut = time.time()
                    Solution = algo1(TableauLecture,Taille,espece,nbEsp)
                    temps = time.time() - debut
                if NumAlgo == 2:
                    debut = time.time()
                    Solution = algo2(TableauLecture,Taille,espece,nbEsp)
                    temps = time.time() - debut
                verif = verificateur(TableauLecture,Solution,1,len(Solution),1,espece,Taille,False)
                minorant = Minorant(Taille,nbEsp,espece,TableauLecture)
                if verif == False:
                    print(TEST,"Erreur",ListeFichier[TEST])
                elif verif != False:
                    print(ListeFichier[TEST],";",minorant,";",temps,";",len(Solution))
            else:
                print(ListeFichier[TEST],";","Impossible")

# TestSeul permet de tester un fichier en particulier en mettant nom.txt pour le nom et non l'adresse
# Apercu est un booléen qui permet d'afficher l'aperçu ou non
# Dans ce cas le vérificateur ne nous dira pas juste si la solution est valide ou non, il affichera les causes de l'erreur

def TestSeul(NumAlgo,nom,apercu,k):
    adresse = rep + '\\' + nom
    file = open(adresse,'r')
    (Taille,TableauLecture,espece,nbEsp) = readfile(file)
    if VerifSolutionPossible(Taille,nbEsp,espece,TableauLecture) == True:
        if NumAlgo == 1:
            Solution = algo1(TableauLecture,Taille,espece,nbEsp)
            verificateur(TableauLecture,Solution,1,len(Solution),1,espece,Taille,True)
        if NumAlgo == 2:
            Solution = algo2(TableauLecture,Taille,espece,nbEsp)
            verificateur(TableauLecture,Solution,1,len(Solution),1,espece,Taille,True)
        if NumAlgo == 3:
            Solution = AlgoRectangle(TableauLecture,Taille,espece,nbEsp,k)
            if Solution == False:
                print("Pas de solution possible avec cet algorithme")
                return
            verificateur(TableauLecture,Solution,k,len(Solution),2,espece,Taille,True)
        minorant = Minorant(Taille,nbEsp,espece,TableauLecture)
        if apercu =="True":
            img = nouvelleImage(Taille,Taille)
            afficheApercu(Taille,TableauLecture,img)
            afficheApercuFinal(Taille,Solution,img)
        print("La solution est :\n",Solution)
        print("Avec",len(Solution),"cases protégée")
    else:
        print("Il est impossible d'atteindre l'objectif de protection pour l'une des espèce")

# Cette partie nous permet de faire nos tests en entrant directement les paramètres dans le terminal
k = 2
TypeTest = input("Entrer le type de test, 'Seul' ou 'All': ")
NumAlgo = int(input("Entrer le numéro de l'algorithme : "))
if NumAlgo > 3:
    print("Il n'y a pas d'algorithme avec ce numéro")
elif TypeTest == "All":
    erreur = input("Entrer True pour afficher tous les noms, False pour afficher seulement ceux qui posent problème : ")
    if NumAlgo == 3:
        k = int(input("Entrer le nombre de zones (de 2 à 7) : "))
    TestAll(NumAlgo,erreur,k)
elif TypeTest == "Seul":
    nom = input("Entrer le nom du fichier sous le format 'archipel_2_10_10_2.txt' par exemple : ")
    apercu = input("Entrer 'True' pour afficher une image des zones protégées : ")
    if NumAlgo == 3:
        k = int(input("Entrer le nombre de zones (de 2 à 7) : "))
    TestSeul(NumAlgo,nom,apercu,k)
else:
    print("Les seuls paramètres possibles sont 'Seul' ou 'All'")

#  archipel_2_10_10_5.txt

#343 fichier à tester

# le secteur de coordonnées (x, y) a pour indice y ∗ Taille + x

# Le secteur d’indice i a pour coordonnées (i mod(Taille),⌊i/Taille⌋)