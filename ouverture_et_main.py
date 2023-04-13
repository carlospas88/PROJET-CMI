apercu = True
# permet l'affichage d'une image si besoin

from bibimages import *
import csv  
from algo1 import *
from EcritureSolution import *
from Verificateur import *

# Ouvrir le fichier csv, lien a changer en fonction du fichier choisi
file = open(r"C:\Users\tomgi\Documents\Projet Optim\smalldata\detroit_2_100_100_5.txt_hard.txt",'r')


def readfile(file,apercu):
    print("Ouverture du fichier ... ")
    fichier = csv.reader(file,delimiter=";") # ouvre le fichier 
    xTab = 0
    yTab = 0
    Taille = 0
    b = 'Oui'
    cptEsp = 0
    numZone = 0
    for row in fichier: # permet de faire une boucle qui lit ligne par ligne le fichier
        
        if b == -1 and yTab != Taille: #assigne les valeurs au tableau qui est créé dans un autre if, le b == -1 signifie que l'on a lus toute les lignes avant les valeurs des cases
            T[yTab][xTab][0] = numZone #assigne le numéro de zone comme première valeur 
            numZone = numZone + 1
            for i in range(1,nbEsp+2):
                T[yTab][xTab][i] = int(row[i+1]) #lis les valeurs terre ou mer, puis le nombre de poissons de chaque ligne et les ajoute au tableau
            xTab += 1 # décale la coordée x de 1
        
        if b == 'Oui': # Permet de lire la toute première ligne, qui correspond au nombre d'espèces à protéger.
            b = int(row[0])+2 # assigne a b le nombre de ligne où l'on a des informations sur les poissons
            nbEsp = int(row[0])
            espece = [0]*nbEsp #créer un tableau où l'on va mettre les quantités de poissons à protéger.
        
        if b > 0: # tant que b>0, on est encore en train de lire les lignes concernant les noms de poissons et la quantité à protéger
            if b!=nbEsp+2 and b!=nbEsp+1: # marche, je ne sais pas trop pourquoi, il y a un décalage de deux, il y a bien un décalage de 1 car ce if est après l'autre ou b est définit, on lit donc la même ligne
                espece[cptEsp] = int(row[1]) #ajoute les valeurs à protéger
                cptEsp = cptEsp +1
            b = b-1
        
        if b == 0 : # quand b = 0, on lit la ligne ou il y a la taille et on peut faire le tableau
            Taille = int(row[0])
            if apercu == True:
                img = nouvelleImage(Taille,Taille) # on fait une image si on veut avoir l'apercu après
            b = b - 1
            T = [0]*Taille # on commence le tableau, une première dimension qui correspond aux colonnes.
            for dy in range(Taille):
                T[dy] = [0]*Taille # on remplace chaque 0 des collones par un tableau qui correspond aux lignes 
                for dz in range(Taille):
                    T[dy][dz] = [0]*(2+nbEsp) # on remplace les 0 des lignes par un tableau avec un nombre suffisant de cases pour mettre toutes les valeurs
        
        if xTab == Taille and b == -1: # quand on arrive au bout de la ligne on passe à la colonne d'après
            xTab = 0
            yTab += 1
    file.close()
    return (Taille,T,espece,nbEsp)

def afficheApercu(Taille,TAp,img): # lit le tableau et regarde la case [1] qui a la valeur Terre/mer
    print("Création de l'image ...")
    for i in range(Taille):
        for j in range(Taille):
            if TAp[i][j][1] == 0 :
                colorierPixel(img,i,j,(255,255,255))
            elif TAp[i][j][1] == 1:
                colorierPixel(img,i,j,(0,0,0))
            else:
                print("La zone (",i,",",j,") n'as pas une valeur correcte, 0 ou 1 (Mer / Terre), sa valeur est de : ",TAp[i][j][1])
    return img

def afficheApercuFinal(Taille,TSol,img): #Affiche les zones protégée 
    print("Affichage final ...")
    q = 0 
    for i in range(len(TSol)):
        i = int(TSol[i])
        y = i%Taille
        x = i//Taille
        colorierPixel(img,x,y,(255,100,100))
    afficherImage(img)

(Taille,T,espece,nbEsp) = readfile(file,apercu)

print("Algo1 ...")
Solution = algo1(T,Taille,espece,nbEsp)

img = nouvelleImage(Taille,Taille)
if apercu ==True:
    afficheApercu(Taille,T,img)
    afficheApercuFinal(Taille,Solution,img)
verificateur(T,Solution,1,len(Solution),1,espece,Taille)
