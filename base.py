import copy
import random


NB_TOURS = 13
AUTOMATIC = False  # A des fins de test, pour jouer aléatoirement

joueurs = []

# caractères de boite
ASCII_VERTICAL = "\u2551"
ASCII_HORIZONTAL = "\u2550"
ASCII_BLHC = "\u255A"
ASCII_BRHC = "\u255D"
ASCII_TLHC = "\u2554"
ASCII_TRHC = "\u2557"

fgcolors = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "light grey": 37,
    "dark grey": 90,
    "white": 97,
}

bgcolors = {k: v + 10 for k, v in fgcolors.items()}


def print_x(s: str, **kwargs) -> None:
    own_kwargs = ["fgcol","bgcol","bold","italic","undeline","blink"]
    fgcol = kwargs["fgcol"] if kwargs.get("fgcol") is not None else None
    bgcol = kwargs["bgcol"] if kwargs.get("bgcol") is not None else None
    bold = kwargs["bold"] if kwargs.get("bold") is not None else False
    italic = kwargs["italic"] if kwargs.get("italic") is not None else False
    underline = kwargs["underline"] if kwargs.get("underline") is not None else False
    blink = kwargs["blink"] if kwargs.get("blink") is not None else False
    rem_kwargs = {k:v for k,v in kwargs.items() if k not in own_kwargs}
    modfs = []
    if fgcol is not None:
        modfs.append(fgcolors[fgcol])
    if bgcol is not None:
        modfs.append(fgcolors[bgcol])
    if bold:
        modfs.append(1)
    if italic:
        modfs.append(3)
    if underline:
        modfs.append(4)
    if blink:
        modfs.append(5)
    modf = ";".join(list(map(str, modfs)))
    gs = "\033[" + modf + "m" + s + "\033[0m"
    print(gs,**rem_kwargs)


def get_user_type(t: object, possible: list[object], **kwargs) -> object:
    """Prend en paramètre une classe `t` et essaie de cast la chaîne de caractères entrée par le joueur en ce type-là"""
    prompt = ">>> "
    for k, v in kwargs.items():
        if k != "prompt":
            raise ValueError(f"Unknown keyword argument '{k}'")
        elif type(v) != str:
            raise TypeError("Prompt must be a string")
        else:
            prompt = v
    if AUTOMATIC:
        return random.choice(possible)
    else:
        s = input(prompt)
    try:
        return t(s)
    except:
        print_x(f"Error: this is not a {t}", fgcol="white", bgcol="red")
        return get_user_type(t, possible, **kwargs)


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
    _des.sort(key=lambda x: des.count(x), reverse=True)
    return _des[2] == _des[0]


def est_carre(des: list[str]) -> bool:
    _des = [d for d in des]
    _des.sort()
    _des.sort(key=lambda x: des.count(x), reverse=True)
    return _des[3] == _des[0]


def est_full(des: list[str]) -> bool:
    _des = [d for d in des]
    _des.sort()
    _des.sort(key=lambda x: des.count(x), reverse=True)
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
    "petite suite": {"type": "contains", "contents": ["1234", "2345", "3456"]},
    "grande suite": {"type": "contains", "contents": ["12345", "23456"]},
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
    "petite suite": {"type": "fixed", "value": 30},
    "grande suite": {"type": "fixed", "value": 40},
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
    return True
