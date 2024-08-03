import copy

NB_TOURS = 13


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


def est_brelan(des: list[str]) -> bool:
    _des = [d for d in des]
    _des.sort()
    print(_des)
    _des.sort(key=lambda x: des.count(x), reverse=True)
    print(_des)
    return _des[2] == _des[0]


def est_carre(des: list[str]) -> bool:
    _des = [d for d in des]
    _des.sort()
    _des.sort(key=lambda x: _des.count(x), reverse=True)
    return _des[3] == _des[0]


def est_full(des: list[str]) -> bool:
    _des = [d for d in des]
    _des.sort()
    _des.sort(key=lambda x: _des.count(x), reverse=True)
    return _des[2] == _des[0] and _des[3] == _des[4]


def est_yams(des: list[int]) -> bool:
    return des == [des[0]] * len(des)


restrictions = {
    "1": {"type": "n_of_a_kind", "kind": 1},
    "2": {"type": "n_of_a_kind", "kind": 2},
    "3": {"type": "n_of_a_kind", "kind": 3},
    "4": {"type": "n_of_a_kind", "kind": 4},
    "5": {"type": "n_of_a_kind", "kind": 5},
    "6": {"type": "n_of_a_kind", "kind": 6},
    "brelan": {"type": "variable", "function": est_brelan},
    "carré": {"type": "variable", "function": est_carre},
    "full": {"type": "variable", "function": est_full},
    "petite_suite": {"type": "contains", "contents": ["1234", "2345", "3456"]},
    "grande_suite": {"type": "contains", "contents": ["12345", "23456"]},
    "yams": {"type": "variable", "function": est_yams},
    "chance": {"type": "any"},
}

scores = {
    "1": {"type": "somme partielle", "kind": 1},
    "2": {"type": "somme partielle", "kind": 2},
    "3": {"type": "somme partielle", "kind": 3},
    "4": {"type": "somme partielle", "kind": 4},
    "5": {"type": "somme partielle", "kind": 5},
    "6": {"type": "somme partielle", "kind": 6},
    "brelan": {"type": "somme"},
    "carré": {"type": "somme"},
    "full": {"type": "fixed", "value": 25},
    "petite_suite": {"type": "fixed", "value": 30},
    "grande_suite": {"type": "fixed", "value": 40},
    "yams": {"type": "fixed", "value": 50},
    "chance": {"type": "somme"},
}


def est_inclus(a: list, b: list) -> bool:
    _b = copy.deepcopy(b)
    for e in a:
        if e in _b:
            _b.pop(_b.index(e))
        else:
            return False
