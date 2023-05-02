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

def TestAll(NumAlgo,erreur):
    for TEST in range(342):
        adresse = rep + '\\' + ListeFichier[TEST]
        file = open(adresse,'r')
        if erreur == "True":
            print("Lecture de :",adresse)
        (Taille,TableauLecture,espece,nbEsp) = readfile(file)
        if VerifSolutionPossible(Taille,nbEsp,espece,TableauLecture) == True:
            if NumAlgo == 1:
                Solution = algo1(TableauLecture,Taille,espece,nbEsp)
            verif = verificateur(TableauLecture,Solution,1,len(Solution),1,espece,Taille,False)
            if verif == False and erreur != "True":
                print("Erreur",adresse)
        else:
            print("Impossible",adresse)

# TestSeul permet de tester un fichier en particulier en mettant nom.txt pour le nom et non l'adresse
# Apercu est un booléen qui permet d'afficher l'aperçu ou non
# Dans ce cas le vérificateur ne nous dira pas juste si la solution est valide ou non, il affichera les causes de l'erreur            
            
def TestSeul(NumAlgo,nom,apercu):
    adresse = rep + '\\' + nom
    file = open(adresse,'r')
    (Taille,TableauLecture,espece,nbEsp) = readfile(file)
    if VerifSolutionPossible(Taille,nbEsp,espece,TableauLecture) == True:
        if NumAlgo == 1:
            Solution = algo1(TableauLecture,Taille,espece,nbEsp)
        verificateur(TableauLecture,Solution,1,len(Solution),1,espece,Taille,True)
        if apercu =="True":
            img = nouvelleImage(Taille,Taille)
            afficheApercu(Taille,TableauLecture,img)
            afficheApercuFinal(Taille,Solution,img)
        print("La solution est :\n",Solution)
        print("Avec",len(Solution),"cases protégée")
    else:
        print("Il est impossible d'atteindre l'objectif de protection pour l'une des espèce")

        
# Cette partie nous permet de faire nos tests en entrant directement les paramètres dans le terminal

TypeTest = input("Entrer le type de test, 'Seul' ou 'All': ")
NumAlgo = int(input("Entrer le numéro de l'algorithme : "))
if NumAlgo > 1:
    print("Il n'y a pas d'algorithme avec ce numéro")
elif TypeTest == "All":
    erreur = input("Entrer True pour afficher tous les noms, False pour afficher seulement ceux qui posent problème : ")
    TestAll(NumAlgo,erreur)
elif TypeTest == "Seul":
    nom = input("Entrer le nom du fichier sous le format 'archipel_2_10_10_2.txt' par exemple : ")
    apercu = input("Entrer 'True' pour afficher une image des zones protégées : ")
    TestSeul(NumAlgo,nom,apercu)
else:
    print("Les seuls paramètres possibles sont 'Seul' ou 'All'")


#343 fichier à tester

# le secteur de coordonnées (x, y) a pour indice y ∗ Taille + x

# Le secteur d’indice i a pour coordonnées (i mod(Taille),⌊i/Taille⌋)
