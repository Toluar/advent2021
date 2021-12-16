#!/usr/bin/env python3


Filin1 = open("Input.4.2","r")
tirages = Filin1.readlines()
Filin1.close()
#On cree un tableau avec la liste des chiffres composant le tirage
tirage = tirages[0].replace("\n","").split(",")

#On recupere ensuite l ensemble des grilles
TailleGrille = 5
Nb_Grilles = 0
Liste_Grille = {} #Dictionnaire contenant l ensemble des grilles
Grille = [[0] * TailleGrille for i in range(TailleGrille)]  #Grille de base
IndLigne = 0 #Va contenir l indice de la ligne que l on va ajouter


filin = open("Input.4","r")
for i,ligneG in enumerate(filin):
    if len(ligneG) > 1:
        #C est une ligne qui doit etre ajouter a la grille
        TableTMP = ligneG.replace("  "," ").split()
        for x in range(len(TableTMP)):
            Val = int(TableTMP[x])
            Grille[IndLigne][x]=Val
        IndLigne += 1
    else:
        #Grille terminee. On passe a une autre grille
        IndLigne = 0
        Liste_Grille[Nb_Grilles]=Grille
        Nb_Grilles +=1
        Grille = [[0] * TailleGrille for i in range(TailleGrille)]
filin.close
Liste_Grille[Nb_Grilles]=Grille
Nb_Grilles +=1

print(f"Nbr de Grilles : {Nb_Grilles}")
print(Liste_Grille)


def Number_in_grille(Grille,Nbr):
    print(f"Taille de la grille : {TailleGrille} ")
    for x in range(0,int(TailleGrille)):
        print(f"{x} => {TailleGrille}")
        for y in range(0,TailleGrille):
            if Grille[x][y] == Nbr:
                Grille[x][y] = "X"
                return True
    return False

def Bingo_in_Grille(Grille):
    #On parcours les lignes.
    #Puis les colonnes
    return False

BINGO = False
for t in range(len(tirage)):
    for i in range(Nb_Grilles):
        if Number_in_grille(Liste_Grille[i],int(tirage[t])):
            BINGO = True

    
# Connaitre le type d une variable : print(type(tirages))


