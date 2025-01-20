""" Procedure qui permet le changement de nom des joueurs

Args:   j1 (str): Nom du joueur 1
        j2 (str): Nom du joueur 2
        val (int): Valeur de changement de nom


"""
def changJoueur(j1:str,j2:str, val:int) -> tuple[str, str]:
                
    if val==1:
        j1=str(input("Entrez le nom du joueur 1: "))
        print("Changement effectué")
        return j1, j2
    if val==2:
        j2=str(input("Entrez le nom du joueur 2: "))
        print("Changement effectué")
        return j1, j2
    else:
        j1=str(input("Entrez le nom du joueur 1: "))
        j2=str(input("Entrez le nom du joueur 2: "))
        print("changement effectué")
        return j1, j2