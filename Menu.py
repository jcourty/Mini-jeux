from Controle import *

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

    tmp=controle(c,1,5)
    if tmp==False:
        c=menu() #fonction récursive si le choix n'est pas dans les bornes. Pour pouvoir retaper un choix
    return c