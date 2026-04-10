alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def pg(positions, filled):
    grid = {p: "-" for p in positions}
    for i, j in filled.items():
        grid[j] = i
    for y in range(4, -1, -1):
        print("".join(" " if (x, y) not in grid else grid[(x, y)] for x in range(6)))

def neigh(a, b):
    return a != b and abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

positions = [(0, 2)] + [(x, y) for x in range(1, 6) for y in range(5)]
filled = {
    "A": (0, 2),
    "D": (2, 4),
    "F": (4, 2),
    "G": (3, 1),
    "J": (2, 3),
    "L": (2, 1),
    "M": (1, 2),
    "S": (5, 0),
    "X": (4, 4),
    "Z": (5, 3),
}

options = {p: [c for c in alphabet if c not in filled] for p in positions if p not in filled.values()}

options[(2,2)].remove("N")
options[(2,2)].remove("I")
options[(2,2)].remove("O")
options[(2,0)].remove("O")

changed = True
while changed:
    changed = False
    pg(positions, filled)
    print()

    for a, b in zip(alphabet, alphabet[1:]):
        for c, d in [(a, b), (b, a)]:
            if c in filled and d not in filled:
                for o in options:
                    if d in options[o] and not neigh(filled[c], o):
                        options[o].remove(d)
                        changed = True

            if c not in filled and d not in filled:
                for o in options:
                    if c in options[o]:
                        if d not in {
                            c2
                            for o2 in options
                            if neigh(o, o2)
                            for c2 in options[o2]
                        }:
                            options[o].remove(c)
                            changed = True
    for c in alphabet:
        if c not in filled:
            poss = [i for i, j in options.items() if c in j]
            if len(poss) == 1:
                filled[c] = poss[0]
                del options[poss[0]]

    #for o in positions:
    #    if o in options and len(options[o]) == 1:
    #        filled[o] = options[o][0]
    #        del options[o]
    #        changed = True
