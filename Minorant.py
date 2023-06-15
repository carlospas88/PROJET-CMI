def Minorant(Taille,nbEsp,Espece,TableauLecture):
    indiceMax = 0
    max = 0
    for i in range(nbEsp):
        if max<Espece[i]:
            max = Espece[i]
            indiceMax = i
    TabTrie = [0]*(Taille**2)
    indice = 0
    for x in range(Taille):
        for y in range(Taille):
            TabTrie[indice] = TableauLecture[x][y][2+indiceMax]
            indice = indice +1
    TabTrie = sorted(TabTrie,reverse=True)
    sommeEspece = 0
    sommeSecteur = 0
    for z in TabTrie:
        sommeEspece = sommeEspece + z
        sommeSecteur = sommeSecteur +1
        if sommeEspece > Espece[indiceMax]:
            return sommeSecteur
