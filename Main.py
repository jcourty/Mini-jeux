import os
from typing import TextIO
from Allumettes import *
from Devinette import *
from Morpion import *
from Menu import *
from Change import *
#from Morpion_full_Ordi import *
#from Morpion_J1_O1 import *

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
    choixbis:int
    choix=0
    tmp:str #variable tempon pour continuer le programme après entrer

    j1=input("Nom du joueur 1: ")
    j2=input("Nom du joueur 2: ")
    os.system('cls' if os.name=='nt' else 'clear')

    print("\033[90m Bienvenue",j1,"et",j2, "dans le ")
    
    while choix!=6:
        choix=menu()

        if choix==1:
            choixbis=camaDeJeu()
            if choixbis!=4:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Bienvenue dans le jeu des devinettes !\n")
                print("Dans ce jeu, l'un de vous devra choisir un nombre secret. L'adversaire devra alors faire des hypothèses sur le nombre, aider des commentaires (plus grand ou plus petit) du joueur.\n")
                print("\033[91mATTENTION, celui qui fait deviner a le droit de tricher trois fois en donnant une mauvaise réponse.")
                print("\033[97mBonne partie!\n")

                if choixbis==1:
                    if j1=="Ordi1": #Si on a fait jouer les ordi ensemble, pour reprendre des noms de joueur normaux
                        j1, j2 =changJoueur(j1,j2,3)
                    if j2=="Ordi1": #Si on a déjà fait des parti contre u ordi, on reprend un nom de joueur normal
                        j1, j2 =changJoueur(j1,j2,2)
                    #fonctionjoueurVSjoueur
                    if devinette(j1,j2)==1:
                        score_j1_devinette = score_j1_devinette + 1
                    else :
                        score_j2_devinette = score_j2_devinette + 1
                    # sert a ne pas afficher le menu direct après
                elif choixbis ==2:
                    if j1=="Ordi1": #Si on a fait jouer les ordi ensemble, pour reprendre des noms de joueur normaux
                        j1, j2 =changJoueur(j1,j2,3)
                    #fonctionjoueurVSOrdi
                    j2="Ordi1"
                    if  devinette(j1,j2)==1:
                        score_j1_devinette = score_j1_devinette + 1
                    else:
                        score_j2_devinette=score_j2_devinette + 1
                elif choixbis==3:
                    j1="Ordi1"
                    j2="Ordi2"
                    devinette(j1,j2)

                tmp=str(input("\033[91mPour continuer, appuyer sur entrée: "))#\033[91m couleur rouge pour le texte 
                os.system('cls' if os.name=='nt' else 'clear')

        elif choix==2:
            choixbis=camaDeJeu()
            if choixbis!=4:
                os.system('cls' if os.name=='nt' else 'clear') #Permet de reinitialisé les écritures sur le terminal
                print("Bienvenue dans le jeu des allumettes !\n")
                print("Les règles du jeu sont les suivantes : Face à vous, vingt allumettes. Votre but? Ne pas ramasser la dernière allumettes pour gagner. Pour cela, vous aurez le choix de retirer une à trois allumettes pour chaque tour.\n")
                print("Bonne chance et que le meilleur gagne!\n")

                if choixbis==1:
                    if j1=="Ordi1": #Si on a fait jouer les ordi ensemble, pour reprendre des noms de joueur normaux
                        j1, j2 = changJoueur(j1,j2,3)
                    if j2=="Ordi1": #Si on a déjà fait des parti contre u ordi, on reprend un nom de joueur normal
                        j1, j2 = changJoueur(j1,j2,2)
                    #fonctionjoueurVSjoueur
                    if allumette(j1,j2)==j1:
                        score_j1_alumettes = score_j1_alumettes + 1
                    else :
                        score_j2_alumettes = score_j2_alumettes + 1
                    # sert a ne pas afficher le menu direct après
                elif choixbis ==2:
                    if j1=="Ordi1": #Si on a fait jouer les ordi ensemble, pour reprendre des noms de joueur normaux
                        j1, j2 =changJoueur(j1,j2,3)
                    #fonctionjoueurVSOrdi
                    j2="Ordi1"
                    if allumette(j1,j2)==j1:
                        score_j1_alumettes = score_j1_alumettes + 1
                    else :
                        score_j2_alumettes = score_j2_alumettes + 1

                elif choixbis==3:
                    j1="Ordi1"
                    j2="Ordi2"
                    allumette(j1,j2)

                tmp=str(input("\033[91mPour continuer, appuyer sur entrée: "))
                os.system('cls' if os.name=='nt' else 'clear')
            
        elif choix==3:
            choixbis=camaDeJeu()
            if choixbis!=4:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Bienvenue dans le jeu du morpion !\n")
                print("Voici les règles du jeu: Le morpion est un jeu contenant deux symboles le X est le O. Votre but est d'aligner trois signes identique dans une grille de 9 cases. Chacun votre tour, il faudra donc déposer votre symboles stratégiquement pour gagner.\n")
                print("Bon jeu et que le meilleur gagne !\n")


                if choixbis==1:
                    if j1=="Ordi1": #Si on a fait jouer les ordi ensemble, pour reprendre des noms de joueur normaux
                        j1, j2 =changJoueur(j1,j2,3)
                    if j2=="Ordi1": #Si on a déjà fait des parti contre u ordi, on reprend un nom de joueur normal
                       j1, j2 =changJoueur(j1,j2,2)

                    miette = jeu_morpion(j1, j2,score_j1_morpion ,score_j2_morpion ) 
                    if miette == 1:
                        score_j1_morpion  = score_j1_morpion  + 1
                    elif miette ==2:
                        score_j2_morpion  = score_j2_morpion  + 1
                elif choixbis==2:
                    #JoueurVSOrdi
                    if j1=="Ordi1": #Si on a fait jouer les ordi ensemble, pour reprendre des noms de joueur normaux
                        j1, j2 =changJoueur(j1,j2,3)
                    j2="Ordi1"
                    """miette = morpionJVSO(j1, j2,score_j1_morpion ,score_j2_morpion ) 
                    if miette == 1:
                        score_j1_morpion  = score_j1_morpion  + 1
                    elif miette ==2:
                        score_j2_morpion  = score_j2_morpion  + 1

                elif choixbis==3:
                    j1="Ordi1"
                    j2="Ordi2"
                    miette = morpionFullPc(j1, j2,score_j1_morpion ,score_j2_morpion ) 
                    if miette == 1:
                        score_j1_morpion  = score_j1_morpion  + 1
                    elif miette ==2:
                        score_j2_morpion  = score_j2_morpion  + 1"""

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
            f.write ('\n')
            f.write ('\n')
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
            print("4-annuler")
            n=int(input("Faites votre choix:")) # Permet aux joueurs de choisir le nom à changer sans devoir retaper les deux
            controle(n,1,4)
            if n!=4:
                if n==1:
                    j1, j2 =changJoueur(j1,j2,1)
                if n==2:
                    j1, j2 =changJoueur(j1,j2,2)
                else:
                    j1, j2 =changJoueur(j1,j2,3)
                
                score_j2_devinette  = 0    #On change de joueur, on remet donc les scores à 0
                score_j1_devinette  = 0
                score_j1_morpion = 0
                score_j2_morpion = 0
                score_j1_alumettes = 0
                score_j2_alumettes = 0
        
    print("A plus dans le bus ",j1,"et",j2,". Au plaisir de vous revoir.")  