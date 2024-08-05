from base import *


def afficher_des(des_conserves: list[int], des_tires: list[int]) -> None:
    print("Dés conservés:", " ".join(map(str, sorted(des_conserves))))
    print("Dés tirés:", " ".join(map(str, sorted(des_tires))))


def init_graphisme():
    # on créé les joueurs
    print("Entrez le nombre de joueurs: ", end="")
    n = get_user_type(int, range(1, 4), prompt="")
    for i in range(n):
        joueurs.append(Joueur(input(f"Nom du {i+1}{'er' if i==0 else 'ème'} joueur: ")))


def afficher_podium(joueurs: list[Joueur]) -> None:
    l = sorted(joueurs, key=lambda x: x.score_total, reverse=True)
    for i in range(len(joueurs)):
        print(f"{i+1}. {l[i]} ({l[i].score_total} pts)")

def get_des():
    return list(
            map(int, input("Quels dés voulez-vous conserver?\n>>> ").split())
        )