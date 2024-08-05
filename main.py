from base import *
from ui import *
from logique import *


def init_partie() -> None:
    """Fonction d'initialisation de la partie"""
    init_logique()
    init_graphisme()


def finir_partie() -> None:
    """Fonction de terminaison de la partie"""
    for j in joueurs:
        j.calculer_scores()
    afficher_podium(joueurs)


def tirage(n: int) -> list[int]:
    """Renvoie une liste de `n` entiers dans [1,6] correspondant donc à un tirage de dés"""
    des_tires = []
    for _ in range(n):
        des_tires.append(random.randint(1, 6))
    return des_tires


def get_des_conserves(des_conserves: list[int], des_tires: list[int]) -> list[int]:
    """Renvoie la liste de dés à garder choisis par le joueur"""
    while not est_inclus(
        des_conserves_choisis := get_des(),
        des_conserves + des_tires,
    ):  # Tant que la liste des dés choisis à conserver n'est pas incluse dans la liste des dés
        print(
            "\033[1;31mChoix impossible, veuillez réessayer\033[0m"
        )  # Afficher un message d'erreur
    return des_conserves_choisis


def get_veut_s_arreter() -> bool:
    """Renvoie un booléen indiquant si le joueur veut s'arrêter"""
    print("Voulez-vous vous arrêter là? (y/N)")
    if get_user_type(
        str,
        ["y", "n"],
    ) in ("y", "Y"):
        return True
    return False


def enregistrement_score(joueur: Joueur, des: list[int]) -> None:
    """Fonction déterminant dans quelle case le joueur veut enregistrer"""
    coups_possibles = list(
        filter(lambda c: joueur.scores[c.nom] is None, Coup.coups_possibles(des))
    )
    print("Que voulez-vous faire?")
    for i in range(len(Coup.coups)):
        match joueur.scores[Coup.coups[i].nom]:
            case 0:
                sc = "x"
            case None:
                sc = ""
            case k:
                sc = str(k)
        if Coup.coups[i] not in coups_possibles:
            print_x("%2d. %12s : %2s" % (i + 1, Coup.coups[i], sc), fgcol="dark grey")
        else:
            print("%2d. %12s : %2s" % (i + 1, Coup.coups[i], sc))

    print(f"{len(Coup.coups)+1}. Barrer quelque chose")
    reponse = get_user_type(
        int,
        list(
            filter(
                lambda i: Coup.coups[i - 1] in coups_possibles,
                range(1, len(Coup.coups) + 1),
            )
        ),
    )
    if 1 <= reponse <= len(Coup.coups):
        # Le choix est existant, il faut vérifier qu'il est valide
        if joueur.scores[Coup.coups[reponse - 1].nom] is None and Coup.coups[
            reponse - 1
        ].est_possible(des):
            joueur.scores[Coup.coups[reponse - 1].nom] = Coup.coups[reponse - 1].score(
                des
            )
        else:
            print("\033[1;31mChoix impossible, veuillez réessayer\033[0m")
            enregistrement_score(joueur, des)
    elif reponse == len(Coup.coups) + 1:
        print("Vous voulez barrer...")
        coups_barrables = list(
            filter(lambda c: joueur.scores[c.nom] is None, Coup.coups)
        )
        for i in range(len(coups_barrables)):
            print(f"{i+1}. {coups_barrables[i]}")
        reponse = get_user_type(
            int,
            list(
                filter(
                    lambda i: Coup.coups[i - 1] in coups_barrables,
                    range(1, len(Coup.coups) + 1),
                )
            ),
        )
        if 1 <= reponse <= len(coups_barrables):
            joueur.scores[coups_barrables[reponse - 1].nom] = 0
    else:
        print_x("Choix impossible, veuillez réessayer", fgcol="red", bold=True)
        enregistrement_score(joueur, des)


def jouer(iTour: int, joueur: Joueur) -> None:
    print(f"\n\033[1;36;1mÀ {joueur.nom} de jouer\033[0m")
    print(f"{iTour+1}{'er' if iTour==0 else 'ème'} tour")
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
