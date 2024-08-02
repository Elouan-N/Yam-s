from constantes import *
from graphisme import *
from logique import *

from random import randint

def tirage(n):
    tirage = []
    for _ in range(n):
        tirage.append(randint(1,6))
    return tirage

def jouer(iTour, joueur):
    des_conserves = []
    for iLance in range(3):
        tirage = tirage(5-len(des_conserves))
        afficher_des(tirage, des_conserves)
        # Le joueur enlève ou met des dés de côté
        # Eventuellement, le joueur d'arrête et indique où il veut mettre les points ou s'il veut barrer


def main():
    init_partie()
    for iTour in range(NB_TOURS):
        for joueur in joueurs:
            jouer(iTour,joueur)
    finir_partie()

if __name__ == "__main__":
    main()
