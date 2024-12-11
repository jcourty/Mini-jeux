"""Fonction qui permet de controler si un nombre saisi se tourve bien dans la borne souhaitée

    Args:
        nb : int : nombre saisi
        borneMin : int : borne minimale
        borneMax : int : borne maximale
    retourne un booléen selon si le nombre est dans la borne ou non
"""
def controle(nb:int,borneMin:int, borneMax:int)->bool:
    if nb<borneMin or nb>borneMax:
        print("Erreur de saisie")
        return False
    else:
        return True