from constantes import *
from graphisme import *
from logique import *
from random import randint

joueurs = []


class Joueur:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.scores = {k: None for k in restrictions.keys()}
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


def tirage(n: int) -> list[int]:
    """Renvoie une liste de n entiers dans [1,6]"""
    des_tires = []
    for _ in range(n):
        des_tires.append(randint(1, 6))
    return des_tires


def get_des_conserves(des_conserves: list[int], des_tires: list[int]) -> list[int]:
    """Renvoie la liste de dés à garder choisis par le joueur"""
    while not est_inclus(
        des_conserves_choisis := list(
            map(int, input("Quels dés voulez-vous conserver?\n>>> ").split())
        ),
        des_conserves + des_tires,
    ):
        print("\033[1;34mChoix impossible, veuillez réessayer")
    return des_conserves_choisis


def get_veut_s_arreter() -> bool:
    if input("Voulez-vous vous arrêter là? (y/N)\n>>> ") == "y":
        return True
    return False


def enregistrement_score(joueur: Joueur, iTour: int):
    pass


def jouer(iTour: int, joueur: Joueur) -> None:
    des_conserves = []
    for iLance in range(3):
        des_tires = tirage(5 - len(des_conserves))
        afficher_des(des_conserves, des_tires)
        if iLance != 3 and not get_veut_s_arreter():
            # Le joueur enlève ou met des dés de côté
            des_conserves = get_des_conserves(des_conserves, des_tires)
        else:
            # Le joueur s'arrête et indique où il veut mettre les points ou s'il veut barrer
            enregistrement_score(joueur, iTour)
            return None


def main():
    init_partie()
    for iTour in range(NB_TOURS):
        for joueur in joueurs:
            jouer(iTour, joueur)
    finir_partie()


if __name__ == "__main__":
    main()
