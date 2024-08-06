from base import *
from logique import *

def afficher_des(des_conserves: list[int], des_tires: list[int]) -> None:
    print("Dés conservés:", end=" ")
    print_x(" ".join(map(str, sorted(des_conserves))), fgcol="magenta", bold=True)
    print("Dés tirés:", end=" ")
    print_x(" ".join(map(str, sorted(des_tires))), fgcol="magenta", bold=True)


def init_graphisme():
    # on créé les joueurs
    print("Entrez le nombre de joueurs: ", end="")
    n = get_user_type(int, range(1, 4), prompt="")
    for i in range(n):
        joueurs.append(Joueur(input(f"Nom du {i+1}{'er' if i==0 else 'ème'} joueur: ")))


def afficher_podium(joueurs: list[Joueur]) -> None:
    l = sorted(joueurs, key=lambda x: x.score_total, reverse=True)
    l += ["",""]
    print_x("PODIUM", fgcol="green", bold=True)
    print()
    print_x("             %7.7s             " % (l[0]), fgcol="green", bold=True)
    print_x("   %7.7s ╔═════════╗ %7.7s  " % (l[1], l[2]), fgcol="green", bold=True)
    print_x(" ╔═════════╣    1    ╠═════════╗", fgcol="green", bold=True)
    print_x(" ║    2    ║         ║    3    ║", fgcol="green", bold=True)
    print()
    print_x("SCORES", fgcol="green", bold=True)
    print()
    for i in range(len(joueurs)):
        print_x(f"{i+1}. {l[i]} ({l[i].score_total} pts)", fgcol="green", bold=True)


def afficher_feuille(joueur: Joueur) -> None:
    print_x("Feuille de score actuelle", fgcol="yellow", bold=True)
    for i in range(len(Coup.coups)):
        match joueur.scores[Coup.coups[i].nom]:
            case 0:
                sc = "XX"
            case None:
                sc = ""
            case k:
                sc = str(k)
        print_x(ASCII_VERTICAL, end=" ", fgcol="yellow", bold=True)
        print(
            "%12s :" % (Coup.coups[i].nom + " " * (12 - len(Coup.coups[i].nom))),
            end=" ",
        )
        print_x("%2s" % (sc) + " " * 5 + ASCII_VERTICAL, fgcol="yellow", bold=True)
    print_x(ASCII_BLHC + ASCII_HORIZONTAL * 23 + ASCII_BRHC, fgcol="yellow", bold=True)


def get_des():
    return list(map(int, input("Quels dés voulez-vous conserver?\n>>> ").split()))
