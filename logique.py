from constantes import *


class Coup:
    coups = []  # Tous les coups possibles

    def __init__(self, nom, restrictions) -> None:
        self.restrictions = restrictions
        self.nom = nom
        Coup.coups.append(self)

    def est_possible(self, des: list[int]) -> bool:
        """Renvoie un booléen indiquant si le lancer de dés correspond au coup"""
        pass

    def score(self, des: list[int]) -> int:
        """Prend en paramètre un lancer de dés correspondant au coup, et renvoie le score obtenu pour ce coup"""
        pass

    @classmethod
    def coups_possibles(cls, des: list[int]):
        c_pos = []
        for c in Coup.coups:
            if c.possible(des):
                c_pos.append(c)
        return c

    def __str__(self) -> str:
        return self.nom

    def __repr__(self) -> str:
        return str(self)


def init_logique():
    # On crée les instances de coup
    for k, restr in restrictions.items():
        Coup(k, restr)
