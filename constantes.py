NB_TOURS = 13


restrictions = {
    "1": {"type": "n_of_a_kind", "kind": 1},
    "2": {"type": "n_of_a_kind", "kind": 2},
    "3": {"type": "n_of_a_kind", "kind": 3},
    "4": {"type": "n_of_a_kind", "kind": 4},
    "5": {"type": "n_of_a_kind", "kind": 5},
    "6": {"type": "n_of_a_kind", "kind": 6},
    "brelan": {"type": "variable", "expr": "aaabc"},
    "carré": {"type": "variable", "expr": "aaaab"},
    "full": {"type": "variable", "expr": "aaabb"},
    "petite_suite": {"type": "variable", "expr": "(1234|2345|3456)."},
    "grande_suite": {"type": "variable", "expr": "12345|23456"},
    "yams": {"type": "variable", "expr": "aaaaa"},
    "chance": {"type": "any"},
}
