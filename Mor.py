from Controle import *

""" Procédure permettant d"afficher la grille du morpion
arguements: grille (list[str]) : reprsente grille du morpion
"""
def aff(grille:list[str]):
    print("     0   1   2 ")    # Défini les colones de la grille 
    print("    ___ ___ ___ ")     
    print("0 ", end='')     # definie la ligne 0
    for i in range (3):
        print(" | " + str(grille[i]), end='')
    print(" |")
    print("   |___|___|___|")    
    print("1 ", end='')     # definie la ligne 1
    for i in range (3):
        print(" | " + str(grille[i+3]), end='')
    print(" |")
    print("   |___|___|___|")    # ligne 2
    print("2 ", end='')     
    for i in range (3):
        print(" | " + str(grille[i+6]), end='')
    print(" |")
    print("   |___|___|___|")


""" 
Procedure permettant de mettre en place le jeu du morpion en lui meme.

arguements: j1 (str) : nom du joueur 1
            j2 (str) : nom du joueur 2
            grille (list[str]) : grille du morpion
            tour (str) : le joueur qui doit jouer
"""
def jeu(grille:list[str], tour:str,j1:str,j2:str):
    col:int
    lig:int

    # le tour du joueur, il choisi sa case
    print("A "+str(tour)," de jouer")
    col=int(input("Entrez le numero de la colonne : "))
    col = controle(col,0,2)
    lig=int(input("Entrez le numero de la ligne : "))
    lig = controle(lig,0,2)
    print("")
    print("Vous avez choisi la case en position (", col, ",", lig, ")")

    # verifier si la case est prise
    while grille[int(col)+int(lig)*3]!=" ":
        aff(grille) # affiche la grille pour pouvoir voir les case vide
        print("Case déjà prise ! choisissez une autre case !")
        col=int(input("Entrez le numero de la colonne : "))
        col= controle(col,0,2)
        lig=int(input("Entrez le numero de la ligne : "))
        lig = controle(lig,0,2)
        print("Vous avez joué la case (", col, ",", lig, ")")
 
    if tour == j1 :
        grille[col + lig *3]="X" # pour que joueur 1 ai toujours la X
    if tour == j2 :
        grille[col + lig*3]="O"  # pour que joueur 1 ai toujours le O
    aff(grille) # Affiche la grille avec le nouveau caractère


"""Procedure permettant de verifier si un joueur a remporter la partie
Args:
    tab (_type_): La grille du morpion.

Returns:
    binaire : si il retourne 1 alors un joueur a remporter la partie.
"""
def gagnant(tab : list[str]):
    
    # teste tout les combinaison de victoire possible 
    if (tab[0]==tab[1]) and (tab[0]==tab[2]) and (tab[0]!=" "): 
        return 1        # Retourne 1 si cette combinaison est respecter 
    if (tab[3]==tab[4]) and (tab[3]==tab[5]) and (tab[3]!=" "):
        return 1 
    if (tab[6]==tab[7]) and (tab[6]==tab[8]) and (tab[6]!=" "):
        return 1
    if (tab[0]==tab[3]) and (tab[0]==tab[6]) and (tab[0]!=" "):
        return 1
    if (tab[1]==tab[4]) and (tab[1]==tab[7]) and (tab[1]!=" "):
        return 1
    if (tab[2]==tab[5]) and (tab[2]==tab[8]) and (tab[2]!=" "):
        return 1
    if (tab[0]==tab[4]) and (tab[0]==tab[8]) and (tab[0]!=" "):
        return 1
    if (tab[2]==tab[4]) and (tab[2]==tab[6]) and (tab[2]!=" "):
       return 1


"""Fonction si il y a match nul
Args:
    grille(list[str]): La grille du morpion

Returns:
    0 / 1 : (1) si match  nul sinon (0)
"""
def match_nul(grille:list[str]):

    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1

def jeu_morpion(j1:str, j2:str, scorej1:int, scorej2:int)-> str:
    joueur : str
    gagne : int
    grille : list[str]
    
    joueur= j1
    gagne=0
    grille=[" ", " "," ", " "," ", " "," ", " "," "]        # Representer le tableau du morpion.
     
    # Montre ce que chaque joueur joue comme caractère.
    print("\033[91mX \033[97mpour ",j1,". \033[91m0 \033[97mpour ",j2,".") #\033[91m, \033[97m pour mettre de la couleur 
    aff(grille)     # permet d'afficher la grille du morpion.
    
    while gagne == 0:
        jeu(grille, joueur, j1, j2 )        # permet au joueur de placer son caractère sur la grille 
        if gagnant(grille):     # teste si il y a une combinaison gagnante.
            print("Bravo"+ str(joueur) + " vous avez gagné !! ")    # Annonce le gagnant de la partie. 
            # Faire les scores de chaque joueur 
            if joueur == j1 : 
                scorej1 = scorej1 + 1
                print(scorej1, "pour", j1)
                print(scorej2, "pour", j2)
                return j1
            else:
                score_j2 = scorej2 + 1
                print(scorej1, "pour", j1)
                print(score_j2, "pour", j2)
                return j2
            
        else:       # teste si il y a un match nul.
            if match_nul(grille):
                print("Match nul !")
                gagne=1
            
        # permet de definir le tour de chaque joueur.
        if joueur == j1:
            joueur = j2
        else:
            joueur = j1  
    return " Personne "

"""
if __name__=="__main__":
    c:str
    joueur1:str
    joueur2:str

    joueur1=input("Nom du joueur 1: ")
    joueur2=input("Nom du joueur 2: ")

    c=jeu_morpion(joueur1, joueur2, 0, 0)
    print(c)
"""