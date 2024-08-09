from base import *
import itertools
import tqdm
import time


class Coup:
    coups = []  # Tous les coups possibles

    def __init__(self, nom, restrictions, score) -> None:
        self._restrictions = restrictions
        self._score = score
        self.nom = nom
        Coup.coups.append(self)

    def est_possible(self, des: list[int]) -> bool:
        """Renvoie un booléen indiquant si le lancer de dés correspond au coup"""
        match self._restrictions["type"]:
            case "n_of_a_kind":
                return self._restrictions["kind"] in des
            case "variable":
                return self._restrictions["function"](des)
            case "contains":
                for c in self._restrictions["contents"]:
                    if est_inclus(list(map(int, c)), des):
                        return True
                return False

            case _:
                return True

    def score(self, des: list[int]) -> int:
        """Prend en paramètre un lancer de dés correspondant au coup, et renvoie le score obtenu pour ce coup"""
        match self._score["type"]:
            case "somme":
                return sum(des)
            case "somme partielle":
                return sum(filter(lambda x: x == self._score["kind"], des))
            case "fixed":
                return self._score["value"]

    @staticmethod
    def coups_possibles(des: list[int]) -> list["Coup"]:
        c_pos = []
        for c in Coup.coups:
            if c.est_possible(des):
                c_pos.append(c)
        return c_pos

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        return str(self)


class Joueur:
    def __init__(self, nom) -> None:
        self.nom = nom
        self.scores = {k: None for k in restrictions.keys()}
        self.score_inf = 0
        self.score_sup = 0
        self.bonus = False
        self.score_total = 0

    def calculer_scores(self):
        self.score_sup = sum(v for k, v in self.scores.items() if k.isdigit())
        if self.score_sup >= 63:
            self.bonus = True
        self.score_inf = sum(v for k, v in self.scores.items() if not k.isdigit())
        self.score_total = self.score_sup + self.bonus * self.score_inf + self.score_inf

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        return str(self)


probas = {}


def init_probas():
    """bla"""  # TODO
    for i in range(1, 6):
        l = sorted(
            list(
                map(
                    lambda x: tuple(sorted(list(x))),
                    itertools.product(range(1, 7), repeat=i),
                )
            )
        )
        n = len(l)
        for e in l:
            if probas.get(e) is None:
                probas[e] = l.count(e) / n


# class ArbreDecision:
#     """Classe servant à représenter et stocker les décisions prises par l'IA"""

#     etats = []

#     def __init__(self, des: list[int], nbLancersRestants: 0 | 1 | 2):
#         self.des = des
#         self.nbLancersRestants
#         self.fils = []
#         self.score = None
#         self.a_garder = (
#             []
#         )  # Dés à garder, après consultation de toutes les possibilités

#     def __equal__(self, other):
#         return self.nbLancersRestants == other.nbLancersRestants and sorted(
#             self.des
#         ) == sorted(other.des)


class IA(Joueur):
    def __init__(self, nom: str, niveau=0):
        super(IA, self).__init__(nom)
        self.niveau = niveau

    def meilleur_coup(self, des: list[int]) -> Coup | None:
        c_pos = list(
            filter(lambda c: self.scores[c.nom] is None, Coup.coups_possibles(des))
        )
        if c_pos != []:
            return max(c_pos, key=lambda c: c.score(des))

    def calculer_score_espere_et_des_a_garder(
        self, des: list[int], nbLancerRestants: 0 | 1 | 2
    ) -> tuple[list[int], int | float]:
        if nbLancerRestants == 0:
            return (
                des,
                c.score(des) if (c := self.meilleur_coup(des)) is not None else 0,
            )
        # liste des couples (dés gardés, score obtenu en moyenne avec ces dés)
        scores_obtenus: list[tuple[list[int], float]] = []

        # Etape 1: je constitue la liste des liste de dés que je peux garder et supprime les doublons
        for i in range(5, -1, -1):
            # On calcule les sous-ensembles de taille `i` de des et on supprime les doublons
            des_a_garder_poss: list[list[int]] = list(
                map(
                    lambda l: sum([[i + 1] * l[i] for i in range(6)], start=[]),
                    set(
                        map(
                            lambda l: tuple([l.count(i + 1) for i in range(6)]),
                            itertools.combinations(des, i),
                        )
                    ),
                )
            )
            # Pour chacun, je simule tous les tirages possibles des autres dés et pareil une deuxième fois si je suis au premier lancer
            nouveaux_des = list(
                map(list, itertools.combinations_with_replacement(range(1, 7), 5 - i))
            )
            for dg in des_a_garder_poss:
                # Je calcule le score obtenu à l'extrémité de chaque branche et je moyenne en remontant
                score = 0
                nb_nd = 0
                for nd in nouveaux_des:
                    nb_nd += 1
                    score += self.calculer_score_espere_et_des_a_garder(
                        dg + nd, nbLancerRestants - 1
                    )[1]
                score /= nb_nd
                scores_obtenus.append((list(dg), score))
        return max(scores_obtenus, key=lambda x: x[1])

    def meilleure_action(self, des: list[int], iLance: int):
        """Input:
        - liste des 5 dés
        - indice du tirage (entre 0 et 2)

        Output:
        - les réponses dans l'ordre
            - `'y'` ou `'n'` (si on veut s'arrêter)
            - l'indice de coup à marquer (int) ou les dés a conserver (str)
            - si on doit barrer, l'indice du coup à barrer(int)"""


def init_logique():
    # On crée les instances de coup
    for k, restr in restrictions.items():
        Coup(k, restr, scores[k])


if __name__ == "__main__":
    init_logique()
    ordi1 = IA("ordi1")
    combinaison = [1, 1, 1, 1, 1]
    print(combinaison)
    temps_a = time.monotonic()
    print(ordi1.calculer_score_espere_et_des_a_garder(combinaison, 2))
    print(f"temps: {round(time.monotonic() - temps_a, 1)} sec")
