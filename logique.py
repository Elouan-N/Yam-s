from constantes import *


class Coup:
    coups = []  # Tous les coups possibles

    def __init__(self, nom, restrictions):
        self.restrictions = restrictions
        self.nom = nom

    def possible(self, des):
        """Renvoie un booléen indiquant si le lancer de dés correspond au coup"""

    def score(self, des):
        """Prend en paramètre un lancer de dés correspondant au coup, et renvoie le score obtenu pour ce coup"""

    @classmethod
    def coups_possibles(cls, des):
        c_pos = []
        for c in Coup.coups:
            if c.possible(des):
                c_pos.append(c)
        return c

    def __str__(self):
        return self.nom

    def __repr__(self):
        return str(self)
