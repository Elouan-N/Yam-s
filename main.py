from constantes import *
from graphisme import *
from logique import *


def jouer():
    pass


def main():
    init_partie()
    for iTour in range(NB_TOURS):
        for joueur in joueurs:
            jouer(iTour,joueur)
    finir_partie()
