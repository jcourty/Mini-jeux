import getpass

import os
from typing import TextIO

def controle(nb:int,borneMin:int, borneMax:int)->bool:
    if nb<borneMin or nb>borneMax:
        print("Erreur de saisie")
        return False
    else:
        return True
    
def allumette(j1 : str, j2 : str)->str:
    choix : int         #Choix du nombre d'allumettes a retirer
    alu : int           #Compte les allumettes
    nb_alu : str        #Affichage des allumettes
    start : int         #Définition du premier joueur et du deuxième joueur

    start = 0
    while start<1 or start>2 :
        start = int(input("Quel joueur va commencer : "))
    second : int
    if start == 1 :
        second = 2
    else :
        second = 1
    turn : int          #Compteur de tours
    nb_alu = ""
    alu = 20
    turn = 1

    for i in range(0, alu) :    #Remplis la variable pour y mettre le bon nombre d'allumettes
        nb_alu = nb_alu+"| "

    print (nb_alu)          #Affiche la quantité d'allumettes sous forme de batônnets
    print (alu)             #Affiche la quantité d'allumettes sous forme numérique

    while alu > 1 :
        if turn//2 :        #Décide de qui va jouer selon le tour actuel
            print ("Joueur", second, ", c'est à vous de jouer")
        else :
            print ("Joueur", start, ", c'est à vous de jouer")
        choix = int(input("Choisissez le nombre d'allumettes à retirer : "))

        if controle(choix,1,3) == True :    #Vérification que le nombre choisit est possible
            alu = alu-choix
            choix = 0                       #Reset du nombre à choisir
            nb_alu = ""                     #Reset de l'affichage des allumettes
            for i in range(0, alu) :
                nb_alu = nb_alu+"| "
            print(nb_alu)
            print(alu)
            turn = turn+1
        else :
            print("Veuillez choisir un nombre entre 1 et 3")    #Répétition de la question si le choix a mal été fait

    if start == 1 :         #Définits le vainqueur selon le tour actuel et le joueur qui a commencé
        if turn//2 == 0:
            print (j2, "a perdu !", j1, "Gagne 1 point")
            return j1
        else :
            print (j1, "a perdu !", j2, "Gagne 1 point")
            return j2
    else :
        if turn//2 == 0:
            print (j1, "a perdu !", j2, "Gagne 1 point")
            return j2
        else :
            print (j2, "a perdu !", j1, "Gagne 1 point")
            return j1
        
def devinette (j1 : str, j2 : str) ->int:
    turn : int
    n : int
    devine : str    #Joueur qui va deviner
    dev: str        #Joueur qui fait deviner
    n2 : int        #Proposition du joueur qui devine
    choix : int     #pour dire si le nombre est inférieur ou supérieur au nombre à deviner
    triche : int    #Compteur de triches, trois triches autorisées maximum
    
    n2 = -1
    choix = 0
    triche = 0
    start = int(input("Saisissez le joueur qui fait devinner (1 ou 2): "))
    tmp=controle(start, 0, 3)
    while tmp == False :
        start = int(input("Saisissez le joueur qui fait devinner (1 ou 2): "))

    n = 1001
    turn=0
    if start == 1 :
        devine = j2
        dev = j1
    else :
        devine = j1
        dev = j2

    while controle(n,0,1000) == False:
        print(dev)
        n = int(getpass.getpass(prompt="Saisissez votre nombre entre 0 et 1000 : ", stream=None))
    
    while n2!=n and turn !=20 :
        turn = turn+1           #Comptage des tours
        print ("Tour : ", turn)
        if start == 1 :        #Si joueur 1 fait deviner
            print(devine)
            n2 = int(input("Essayez un nombre : "))
            choix = 0 #pour reset le choix dans la boucle
            while choix == 0 and n2!=n :
                print(start)
                choix = int(input("Tapez 1 si l'essai est supérieur à votre nombre. Tapez 2 si c'est l'inverse : "))
                if choix == 1 :
                    print("Le nombre de", j2, "est supérieur à celui de", j1)
                    if n2<n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà triché trois fois")
                            print(j1," a triché trop de fois. ", j2," vous gagner cette partie.")
                            return 2
                elif choix == 2 :
                    print("Le nombre de", j2, "est inférieur à celui de", j1)
                    if n2>n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà triché trois fois")
                            print(j1," a triché trop de fois. ", j2," vous gagner cette partie.")
                            return 2
                else :
                    choix = 0
        elif start == 2 :      #Si Joueur 2 fait deviner
            print(devine)
            n2 = int(input("Essayez un nombre : "))
            choix = 0
            while choix == 0 and n2!=n :
                print(start)
                choix = int(input("Tapez 1 si l'essai est supérieur à votre nombre. Tapez 2 si c'est l'inverse : "))
                if choix == 1 :
                    print("Le nombre de", j1, "est supérieur à celui de", j2)
                    if n2<n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà tricher trois fois")
                            print(j2," a triché trop de fois. ", j1," vous gagner cette partie.")
                            return 1
                elif choix == 2 :
                    print("Le nombre de", j1, "est inférieur à celui de", j2)
                    if n2>n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà tricher trois fois")
                            print(j2," a triché trop de fois. ", j1," vous gagner cette partie.")
                            return 1
                else :
                    choix = 0
    if n2 == n :        #Victoire de celui qui devine
        print("Bravo, ", devine, "a deviné le nombre de", start, "en", turn, "tours !")
        print(start, "a tricher", triche, "fois.")

    elif turn == 20 :   #Victoire de celui qui fait deviner
        print("Bravo, ", devine, "n'a pas deviné le nombre de", start, '!')
        print(start, "a tricher", triche, "fois.")
    if start==1 :
        return 2
    else :
        return 1 

def count20(val:int,min:int,max:int):
    while val<min or val>max :
        print("Erreur")
        val = int(input("Saisir la valeur"))
    return val

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

def jeu(grille:list[str], tour:str,j1:str,j2:str):
    col:int
    lig:int

    # le tour du joueur, il choisi sa case
    print("A "+str(tour)," de jouer")
    col=int(input("Entrez le numero de la colonne : "))
    col = count20(col,0,2)
    lig=int(input("Entrez le numero de la ligne : "))
    lig = count20(lig,0,2)
    print("")
    print("Vous avez choisi la case en position (", col, ",", lig, ")")

    # verifier si la case est prise
    while grille[int(col)+int(lig)*3]!=" ":
        aff(grille) # affiche la grille pour pouvoir voir les case vide
        print("Case déjà prise ! choisissez une autre case !")
        col=int(input("Entrez le numero de la colonne : "))
        col= count20(col,0,2)
        lig=int(input("Entrez le numero de la ligne : "))
        lig = count20(lig,0,2)
        print("Vous avez joué la case (", col, ",", lig, ")")
 
    if tour == j1 :
        grille[col + lig *3]="X" # pour que joueur 1 ai toujours la X
    if tour == j2 :
        grille[col + lig*3]="O"  # pour que joueur 1 ai toujours le O
    aff(grille) # Affiche la grille avec le nouveau caractère

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

def match_nul(grille:list[str]):

    for i in range(9):
        if grille[i]==" ":
            return 0
    return 1

def jeu_morpion(j1:str, j2:str, scorej1:int, scorej2:int)-> int:
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
                return 1
            else:
                score_j2 = scorej2 + 1
                print(scorej1, "pour", j1)
                print(score_j2, "pour", j2)
                return 2
            
        else:       # teste si il y a un match nul.
            if match_nul(grille):
                print("Match nul !")
                gagne=1
            
        # permet de definir le tour de chaque joueur.
        if joueur == j1:
            joueur = j2
        else:
            joueur = j1  
    return 3

options = {
    1: "Devinettes       ",
    2: "Allumettes       ",
    3: "Morpion          ",
    4: "Score            ",
    5: "changer de joueur",
    6: "Quitter          "
}

def fantaisie():
    print("\033[93m ___   ___    \033[92m ______    \033[94m __   __    \033[91m __    __")
    print("\033[93m|   \\_/   |   \033[92m|   ___|   \033[94m|  \\ |  |   \033[91m|  |  |  |")
    print("\033[93m|         |   \033[92m|  |___    \033[94m|   \\|  |   \033[91m|  |  |  |")
    print("\033[93m|  |\\_/|  |   \033[92m|   ___|   \033[94m|       |   \033[91m|  |  |  |") #\\ obligatoire pour etre concidéré comme un \ et pas comme un commande
    print("\033[93m|  |   |  |   \033[92m|  |___    \033[94m|  |\\   |   \033[91m|  |__|  |")
    print("\033[93m|__|   |__|   \033[92m|______|   \033[94m|__| \\__|   \033[91m|________|")
    print("\033[97m")

def menu()->int:
    c:int
    tmp:bool

    fantaisie()
    print(" \033[90m____________________________________________ ")
    print("|                                            |")
    for i in options:
        print("|              ",i,"-",options[i],"              |")
    print("|____________________________________________|")
    c=int(input("\033[97mQue voulez vous faire: "))

    tmp=controle(c,1,6)
    if tmp==False:
        c=menu() #fonction récursive si le choix n'est pas dans les bornes. Pour pouvoir retaper un choix
    return c



if __name__=="__main__":
    f : TextIO
    score_j1_devinette : int
    score_j2_devinette  : int
    score_j1_morpion : int
    score_j2_morpion  : int
    score_j1_alumettes : int
    score_j2_alumettes  : int
    
    score_j2_devinette  = 0
    score_j1_devinette  = 0
    score_j1_morpion = 0
    score_j2_morpion = 0
    score_j1_alumettes = 0
    score_j2_alumettes = 0
    j1:str
    j2:str
    aui:str
    choix:int
    choix=0
    tmp:str #variable tempon pour continuer le programme après entrer

    j1=input("Nom du joueur 1: ")
    j2=input("Nom du joueur 2: ")
    os.system('cls' if os.name=='nt' else 'clear')

    print("\033[90m Bienvenue",j1,"et",j2, "dans le ")
    
    while choix!=6:
        choix=menu()

        if choix==1:
            os.system('cls' if os.name=='nt' else 'clear')
            print("Bienvenue dans le jeu des devinettes !\n")
            print("Dans ce jeu, l'un de vous devra choisir un nombre secret. L'adversaire devra alors faire des hypothèses sur le nombre, aider des commentaires (plus grand ou plus petit) du joueur.\n")
            print("\033[91mATTENTION, celui qui fait deviner à le droit de tricher trois fois en donnant une mauvaise réponse.")
            print("\033[97mBonne partie!\n")

            
            if devinette(j1,j2)==1:
                score_j1_devinette = score_j1_devinette + 1
            else :
                score_j2_devinette = score_j2_devinette + 1
            # sert a ne pas afficher le menu direct après 
            tmp=str(input("\033[91mPour continuer, appuyer sur entrée: "))#\033[91m couleur rouge pour le texte 
            os.system('cls' if os.name=='nt' else 'clear')
        
        elif choix==2:
            os.system('cls' if os.name=='nt' else 'clear') #Permet de reinitialisé les écritures sur le terminal
            print("Bienvenue dans le jeu des allumettes !\n")
            print("Les règles du jeu sont les suivantes : Face à vous, vingt allumettes. Votre but? Ne pas ramasser la dernière allumettes pour gagner. Pour cela, vous aurez le choix de retirer une à trois allumettes pour chaque tour.\n")
            print("Bonne chance et que le meilleur gagne!\n")
            
            if allumette(j1,j2)==j1:
                score_j1_alumettes = score_j1_alumettes + 1
            else :
                score_j2_alumettes = score_j2_alumettes + 1

            tmp=str(input("\033[91mPour continuer, appuyer sur entrée: "))
            os.system('cls' if os.name=='nt' else 'clear')
            
        elif choix==3:
            os.system('cls' if os.name=='nt' else 'clear')
            print("Bienvenue dans le jeu du morpion !\n")
            print("Voici les règles du jeu: Le morpion est un jeu contenant deux symboles le X est le O. Votre but est d'aligner trois signes identique dans une grille de 9 cases. Chacun votre tour, il faudra donc déposer votre symboles stratégiquement pour gagner.\n")
            print("Bon jeu et que le meilleur gagne !\n")

            miette = jeu_morpion(j1, j2,score_j1_morpion ,score_j2_morpion ) 
            if miette == 1:
                score_j1_morpion  = score_j1_morpion  + 1
            elif miette ==2:
                score_j2_morpion  = score_j2_morpion  + 1

            tmp=str(input("\033[91mPour continuer, appuyer sur entrée: "))
            os.system('cls' if os.name=='nt' else 'clear')

        if choix==4:
            f = open('Score.txt', 'w')  # permet d'ouvrir le fichier pour pouvoir ecrire dedans
            # écrit le score pour le jeu de devinette
            f.write('Devinette : ')
            f.write ('\n')
            f.write (j1)
            f.write (': ' + str(score_j1_devinette))
            f.write ('\n')
            f.write (j2)
            f.write (': ' + str(score_j2_devinette)) 
            f.write ('\n')
            f.write ('\n')
            # écrit le score pour le jeu des alumettes
            f.write('Alumettes : ')
            f.write ('\n')
            f.write (j1)
            f.write (': ' + str(score_j1_alumettes))
            f.write ('\n')
            f.write (j2)
            f.write (': ' + str(score_j2_alumettes)) 
            # écrit le score pour le jeu du morpions
            f.write('Morpions : ')
            f.write ('\n')
            f.write (j1)
            f.write (': ' + str(score_j1_morpion))
            f.write ('\n')
            f.write (j2)
            f.write (': ' + str(score_j2_morpion)) 
            f.write ('\n')
            f.write ('\n')
            f.close() 
            # affichage du fichier scores.txt 
            print("Tableau des scores : ")
            print("")
            f = open('Score.txt','r')
            # affiche le contenu du fichier
            message = f.read()
            print(message)
            f.close()
            print("")

            tmp=str(input("\033[91mPour continuer, appuyer sur entrée: "))
            os.system('cls' if os.name=='nt' else 'clear')

        if choix==5:
            print("1-changer le nom du joeueur 1")
            print("2-changer le nom du joueur 2")
            print("3-changer les deux")
            n=int(input("Faites votre choix:")) # Permet aux joueurs de choisir le nom à changer sans devoir retaper les deux
            controle(n,1,3) 
            if n==1:
                j1=str(input("Nouveau nom du joueur 1: "))
                print("Changement effectué")
            if n==2:
                j2=str(input("Nouveau nom du joueur 2: "))
                print("Changement effectué")
            else:
                j1=str(input("Nouveau nom du joueur 1: "))
                j2=str(input("Nouveau nom du joueur 2: "))
                print("changement effectué")
                
            score_j2_devinette  = 0    #On change de joueru, on remet donc les scores à 0
            score_j1_devinette  = 0
            score_j1_morpion = 0
            score_j2_morpion = 0
            score_j1_alumettes = 0
            score_j2_alumettes = 0
        
    print("A plus dans le bus ",j1,"et",j2,". Au plaisir de vous revoir.")  
