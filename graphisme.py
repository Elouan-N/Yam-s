from constantes import *


def afficher_des(des_conserves: list[int], des_tires: list[int]) -> None:
    print("Dés conservés:", " ".join(map(str, sorted(des_conserves))))
    print("Dés tirés", " ".join(map(str, sorted(des_tires))))


def init_graphisme():
    pass
