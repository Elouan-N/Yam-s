from constantes import *
from graphisme import *
from logique import *
from random import randint
import copy

joueurs = []

class Joueur:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.scores = {k:None for k in restrictions.keys()}
        self.score_inf = 0
        self.score_sup = 0
        self.score_total = 0

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        return str(self)

def init_partie():
    init_logique()
    init_graphisme()

def finir_partie():
    pass

def tirage(n):
    des_tires = []
    for _ in range(n):
        des_tires.append(randint(1,6))
    return des_tires

def est_inclus(a :list, b :list) -> bool:
    """Renvoie True ssi a est inclus dans b"""
    _b = copy.deepcopy(b)
    for elt in a:
        if elt not in _b:
            return False
        else:
            _b.pop(_b.index(elt))
    return True

def get_des_conserves(des_conserves, des_tires):
    while not est_inclus(des_conserves_choisis := list(map(int, input("Quels dés voulez-vous conserver?\n>>> ").split())),des_conserves+des_tires) :
        print("Choix impossible, veuillez réessayer")
    return des_conserves_choisis

def jouer(iTour, joueur):
    des_conserves = []
    for iLance in range(3):
        des_tires = tirage(5-len(des_conserves))
        afficher_des(des_conserves, des_tires)
        # Le joueur enlève ou met des dés de côté
        des_conserves = get_des_conserves(des_conserves, des_tires)
        # Eventuellement, le joueur s'arrête et indique où il veut mettre les points ou s'il veut barrer


def main():
    init_partie()
    for iTour in range(NB_TOURS):
        for joueur in joueurs:
            jouer(iTour,joueur)
    finir_partie()

if __name__ == "__main__":
    main()
