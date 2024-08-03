from constantes import *


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

    @classmethod
    def coups_possibles(cls, des: list[int]) -> list['Coup']:
        c_pos = []
        for c in Coup.coups:
            if c.est_possible(des):
                c_pos.append(c)
        return c_pos

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        return str(self)


def init_logique():
    # On crée les instances de coup
    for k, restr in restrictions.items():
        Coup(k, restr, scores[k])
