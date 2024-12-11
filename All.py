from Controle import controle

"""Fonction qui permet de jouer au jeu des allumettes

    Args:
        j1 : str : Nom du joueur 1
        j2 : str : Nom du joueur 2
    retourne une chaine de caractère qui correspond au nom du joueur qui a gagné
"""
def allumette(j1 : str, j2 : str)->str:
    choix : int         #Choix du nombre d'allumettes retirées
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

    for i in range(0, alu) :    #Remplis la viriable pour y mettre le bon nombre d'allumettes
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