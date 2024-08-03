from constantes import *


def afficher_des(des_conserves: list[int], des_tires: list[int]) -> None:
    print("Dés conservés:", " ".join(map(str, sorted(des_conserves))))
    print("Dés tirés", " ".join(map(str, sorted(des_tires))))


def init_graphisme():
    pass


def afficher_podium(joueurs: list[Joueur]) -> None:
    l = sorted(joueurs, key=lambda x: x.score_total, reverse=True)
    for i in range(3):
        print(f"{i+1}. {l[i]}")
