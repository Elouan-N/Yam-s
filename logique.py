from base import *


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

class IA(Joueur):
    def __init__(self,nom,niveau = 0):
        super(IA,self).__init__(nom)
        self.niveau = niveau
        
    def meilleur_coup(self, des :list[int]) -> Coup:
        return max(Coup.coups_possibles(des),key=lambda c:c.score(des))
    
    def meilleure_action(self, des :list[int], iLance :int) -> tuple[str,str] | tuple[str,int] | tuple[str,int,int]:
        """Input:
        - liste des 5 dés
        - indice du tirage (entre 0 et 2)
        
        Output:
        - un tuple qui contient les réponses dans l'ordre
            - `'y'` ou `'n'` (si on veut s'arrêter)
            - l'indice de coup à marquer (int) ou les dés a conserver (str)
            - si on doit barrer, l'indice du coup à barrer(int)"""
        if iLance == 2:
            pass

def init_logique():
    # On crée les instances de coup
    for k, restr in restrictions.items():
        Coup(k, restr, scores[k])
