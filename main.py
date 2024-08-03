from constantes import *
from graphisme import *
from logique import *
from random import randint

joueurs = []


def init_partie():
    init_logique()
    init_graphisme()


def finir_partie():
    for j in joueurs:
        j.calculer_scores()
    afficher_podium(joueurs)


def tirage(n: int) -> list[int]:
    """Renvoie une liste de `n` entiers dans [1,6]"""
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
        print("\033[1;31;1mChoix impossible, veuillez réessayer\033[1;0m")
    return des_conserves_choisis


def get_veut_s_arreter() -> bool:
    """Renvoie un booléen indiquant si le joueur veut s'arrêter"""
    if input("Voulez-vous vous arrêter là? (y/N)\n>>> ") in ("y", "Y"):
        return True
    return False


def enregistrement_score(joueur: Joueur, des: list[int]):
    print("Que voulez-vous faire?")
    coups_possibles = list(filter(lambda c:joueur.scores[c.nom] is None,Coup.coups_possibles(des)))
    for i in range(len(coups_possibles)):
        print(f"{i+1}. {coups_possibles[i]}")
    print(f"{len(coups_possibles)+1}. je barre qqch")
    reponse = int(input(">>> "))
    if 1<=reponse<=len(coups_possibles):
        joueur.scores[coups_possibles[reponse]] = coups_possibles[reponse].score(des)
    elif reponse == len(coups_possibles)+1:
        print("Vous voulez barrer...")
        coups_barrables = list(filter(lambda c:joueur.scores[c.nom] is None,Coup.coups))
        for i in range(len(coups_barrables)):
            print(f"{i+1}. {coups_barrables[i]}")
        reponse = int(input(">>> "))
        if 1<=reponse<=len(coups_barrables):
            joueur.scores[coups_barrables[reponse]] = 0
    else:
        print("\033[1;31;1mChoix impossible, veuillez réessayer\033[1;0m")


def jouer(iTour: int, joueur: Joueur) -> None:
    des_conserves = []
    for iLance in range(3):
        des_tires = tirage(5 - len(des_conserves))
        afficher_des(des_conserves, des_tires)
        if iLance < 2 and not get_veut_s_arreter():
            # Le joueur enlève ou met des dés de côté
            des_conserves = get_des_conserves(des_conserves, des_tires)
        else:
            # Le joueur s'arrête et indique où il veut mettre les points ou s'il veut barrer
            enregistrement_score(joueur, des_tires + des_conserves)
            return None


def main():
    init_partie()
    for iTour in range(NB_TOURS):
        for joueur in joueurs:
            jouer(iTour, joueur)
    finir_partie()


if __name__ == "__main__":
    main()
