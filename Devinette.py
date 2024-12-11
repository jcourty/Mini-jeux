import getpass

"""Fonction qui permet de jouer au jeu de la devinette

    Args:
        j1 : str : Nom du joueur 1
        j2 : str : Nom du joueur 2
    retourne une chaine de caractère qui correspond au nom du joueur qui a gagné
"""

def devinette (j1 : str, j2 : str) ->str:
    turn : int
    n : int
    devine : str    #Joueur qui va deviner
    dev: str       #Joueur qui fait deviner
    n2 : int        #Proposition du joueur qui devine
    choix : int     #pour dire si le nombre est inférieur ou supérieur au nombre à deviner
    triche : int    #Compteur de triches, trois triches autorisées maximum

    n2 = 0
    choix = 0
    triche = 0
    start = int(input("Saisissez le joueur qui fait devinner (1 ou 2): "))
    
    n = 0
    turn=0
    if start == 1 :
        devine = j2
        dev = j1
    else :
        devine = j1
        dev = j2

    while n == 0:
        print(dev)
        n = int(getpass.getpass(prompt="Saisissez votre nombre entre 0 et 1000 : ", stream=None))
        if n>1000 :
            n = 0    
    
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
                            return devine
                elif choix == 2 :
                    print("Le nombre de", j2, "est inférieur à celui de", j1)
                    if n2>n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà triché trois fois")
                            print(j1," a triché trop de fois. ", j2," vous gagner cette partie.")
                            return devine
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
                            return devine
                elif choix == 2 :
                    print("Le nombre de", j1, "est inférieur à celui de", j2)
                    if n2>n or n2==n :
                        triche = triche+1
                        if triche>3 : 
                            choix = 0
                            print("Vous avez déjà tricher trois fois")
                            print(j2," a triché trop de fois. ", j1," vous gagner cette partie.")
                            return devine
                else :
                    choix = 0
    if n2 == n :        #Victoire de celui qui devine
        print("Bravo, ", devine, "a deviné le nombre de", start, "en", turn, "tours !")
        print(start, "a tricher", triche, "fois.")

    elif turn == 20 :   #Victoire de celui qui fait deviner
        print("Bravo, ", devine, "n'a pas deviné le nombre de", start, '!')
        print(start, "a tricher", triche, "fois.")
    return devine