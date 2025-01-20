import getpass
from Controle import controle

"""Fonction qui permet de jouer au jeu de la devinette

    Args:
        j1 : str : Nom du joueur 1
        j2 : str : Nom du joueur 2
    retourne un entier qui correspond au nom du joueur qui a gagné
"""

def devinette (j1 : str, j2 : str) ->int:
    turn : intimport getpass
from Controle import controle
import random

"""Fonction qui permet de jouer au jeu de la devinette

    Args:
        j1 : str : Nom du joueur 1
        j2 : str : Nom du joueur 2
    retourne un entier qui correspond au nom du joueur qui a gagné
"""

def devinette (j1 : str, j2 : str) ->int:
    turn : int
    n : int
    devine : str    #Joueur qui va deviner
    dev: str        #Joueur qui fait deviner
    n2 : int        #Proposition du joueur qui devine
    choix : int     #pour dire si le nombre est inférieur ou supérieur au nombre à deviner
    triche : int    #Compteur de triches, trois triches autorisées maximum
    triche2 : int   #Second compteur, utilisé pour l'ordinateur et vérifier si le joueur à tricher
    x : int         #Variables pour délimiter le choix aléatoire de l'ordinateur s'il devine
    y : int
    
    x=0
    y=1000
    n2 = -1
    choix = 0
    triche = 0
    triche2 = 0

    start = int(input("Saisissez le joueur qui fait devinner (1 ou 2): "))
    while controle(start,1,2) == False :
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
        if dev=='Ordi1' or dev=='Ordi2':    #Vérification de si le joueur est un ordinateur ou non
            n=random.randint(0, 1000)       #Effectue un choix aléatoire
        else :
            n = int(getpass.getpass(prompt="Saisissez votre nombre entre 0 et 1000 : ", stream=None))
    
    while n2!=n and turn !=20 :
        turn = turn+1           #Comptage des tours
        print ("Tour : ", turn)
        if start == 1 :        #Si joueur 1 fait deviner
            print(devine)
            if devine == 'Ordi1' or devine=='Ordi2':    #Vérification de si le joueur est un ordinateur ou non
                n2 = random.randint(x, y)     #Effectue un choix aléatoire entre deux variables
                print(n2)
            else :
                n2 = int(input("Essayez un nombre : "))
            choix = 0 #pour reset le choix dans la boucle
            while choix == 0 and n2!=n :
                print(dev)
                if dev=='Ordi1' or dev=='Ordi2':    #Vérification de si le joueur est un ordinateur ou non
                    if n>n2 :
                        choix = 2
                    else :
                        choix = 1
                else :
                    choix = int(input("Tapez 1 si l'essai est supérieur à votre nombre. Tapez 2 si c'est l'inverse : "))
                if choix == 1 :
                    print("Le nombre de", devine, "est supérieur à celui de", dev)
                    if n2<n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà triché trois fois")      #Défaite du tricher
                            print(j1," a triché trop de fois. ", j2," vous gagner cette partie. Votre nombre était :", n)
                            return 2
                    if triche==triche2 :
                        y=n2-1      #Diminue la limite maximale de l'aléatoire de l'ordinateur
                    triche2=triche

                elif choix == 2 :
                    print("Le nombre de", j2, "est inférieur à celui de", j1)
                    if n2>n or n2==n :
                        triche = triche+1
                        if triche>3 :
                            choix = 0
                            print("Vous avez déjà triché trois fois")      #Défaite du tricher
                            print(j1," a triché trop de fois. ", j2," vous gagner cette partie. Votre nombre était :", n)
                            return 2
                    if triche==triche2 :
                        x=n2+1      #Diminue la limite maximale de l'aléatoire de l'ordinateur
                    triche2=triche
                else :
                    choix = 0
        elif start == 2 :      #Si Joueur 2 fait deviner
            print(devine)
            if devine == 'Ordi1' or devine=='Ordi2':    #Vérification de si le joueur est un ordinateur ou non
                n2 = random.randint(x, y)
                print(n2)
            else :
                n2 = int(input("Essayez un nombre : "))
            choix = 0
            while choix == 0 and n2!=n :
                print(dev)
                if dev=='Ordi1' or dev=='Ordi2':    #Vérification de si le joueur est un ordinateur ou non
                    if n>n2 :
                        choix = 2
                    else :
                        choix = 1
                else :
                    choix = int(input("Tapez 1 si l'essai est supérieur à votre nombre. Tapez 2 si c'est l'inverse : "))
                if choix == 1 :
                    print("Le nombre de", devine, "est supérieur à celui de", dev)
                    if n2<n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà tricher trois fois")      #Défaite du tricheur
                            print(j2," a triché trop de fois. ", j1," vous gagner cette partie. Votre nombre était :", n)
                            return 1
                    if triche==triche2 :
                        y=n2-1      #Diminue la limite maximale de l'aléatoire de l'ordinateur
                    triche2=triche
                elif choix == 2 :
                    print("Le nombre de", j1, "est inférieur à celui de", j2)
                    if n2>n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà tricher trois fois")      #Défaite du tricher
                            print(j2," a triché trop de fois. ", j1," vous gagner cette partie. Votre nombre était :", n)
                            return 1
                    if triche==triche2 :
                        x=n2+1      #Diminue la limite maximale de l'aléatoire de l'ordinateur
                    triche2=triche
                else :
                    choix = 0
    if n2 == n :        #Victoire de celui qui devine
        print("Bravo, ", devine, "a deviné le nombre", n, "de", dev, "en", turn, "tours !")
        print(start, "a tricher", triche, "fois.")

    elif turn == 20 :   #Victoire de celui qui fait deviner
        print("Bravo, ", devine, "n'a pas deviné le nombre de", dev, '!')
        print(dev, "a tricher", triche, "fois.")
        print("Le nombre de", dev, "était :", n)
    if start==1 :
        return 2
    else :
        return 1 
    

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