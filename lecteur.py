import csv  


def readfile(file):
    fichier = csv.reader(file,delimiter=";") # commence à lire le fichier en prenant ";" comme séparateur
    yTab = 0
    xTab = 0
    Taille = 0
    b = 'Oui'
    cptEsp = 0
    for row in fichier: # permet de faire une boucle qui lit ligne par ligne le fichier
        
        if b == -1 and xTab != Taille: #assigne les valeurs au tableau qui est créé dans un autre if, le b == -1 signifie que l'on a lus toute les lignes avant les valeurs des cases
            T[xTab][yTab][0] = yTab*Taille+xTab #assigne le numéro de zone comme première valeur 
            for i in range(1,nbEsp+2):
                T[xTab][yTab][i] = int(row[i+1]) #lis les valeurs terre ou mer, puis le nombre de poissons de chaque ligne et les ajoute au tableau
            yTab += 1 # décale la coordée x de 1
        
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
            b = b - 1
            T = [0]*Taille # on commence le tableau, une première dimension qui correspond aux colonnes.
            for dy in range(Taille):
                T[dy] = [0]*Taille # on remplace chaque 0 des collones par un tableau qui correspond aux lignes 
                for dz in range(Taille):
                    T[dy][dz] = [0]*(2+nbEsp) # on remplace les 0 des lignes par un tableau avec un nombre suffisant de cases pour mettre toutes les valeurs
        
        if yTab == Taille and b == -1: # quand on arrive au bout de la ligne on passe à la colonne d'après
            yTab = 0
            xTab += 1
    file.close()
    return (Taille,T,espece,nbEsp)