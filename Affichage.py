from bibimages import *

def afficheApercu(Taille,TAp,img): # Permet de créer l'image avec les zones de terre et les zones de mer 
    for i in range(Taille):
        for j in range(Taille):
            if TAp[i][j][1] == 0 :
                colorierPixel(img,i,j,(255,255,255))
            elif TAp[i][j][1] == 1:
                colorierPixel(img,i,j,(0,0,0))
            else:
                print("La zone (",i,",",j,") n'as pas une valeur correcte, 0 ou 1 (Mer / Terre), sa valeur est de : ",TAp[i][j][1])
    return img

def afficheApercuFinal(Taille,TSol,img,cas): # Modifie l'image de AfficheApercu pour mettre les zones protégée 
    if cas == 1 or cas == 2:
        for i in range(len(TSol)):
            i = int(TSol[i])
            y = i//Taille
            x = i%Taille
            colorierPixel(img,x,y,(255,100,100))
    if cas == 3 :
        for j in TSol:
            for i in range(len(j)):
                i = int(j[i])
                y = i//Taille
                x = i%Taille
                colorierPixel(img,x,y,(255,100,100))
    afficherImage(img)