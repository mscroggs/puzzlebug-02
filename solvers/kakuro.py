from itertools import product

RED = "\033[31m"
DEFAULT = "\033[0m"

puzzle = """
xx.......x
...x.....x
...x..x...
..xxx.xxx.
......x...
...x......
.xxx.xxx..
...x..x...
x.....x...
x.......xx
"""

aclues = [
    [40],
    [24, 22],
    [6, 4, 9],
    [13],
    [37, 12],
    [12, 36],
    [8],
    [23, 14, 6],
    [15, 7],
    [29],
]
dclues = [
    [30],
    [23, 11],
    [10, 16, 13],
    [11],
    [7, 22],
    [29, 21],
    [8],
    [18, 10, 6],
    [19, 16],
    [41],
]

rows = puzzle.strip().split("\n")

shape = (len(rows), len(rows[0]))


def pretty_print(grid, show_options=False):
    for i in range(shape[0]):
        row = "".join((f"{grid[(i, j)][0]}" if len(grid[(i, j)]) == 1 else f"{RED}{len(grid[(i, j)])}{DEFAULT}") if (i, j) in grid else "#" for j in range(shape[1]))
        if show_options:
            print(row, *["[...]" if len(grid[(i, j)]) > 5 else grid[(i, j)] for j in range(shape[1]) if (i, j) in grid])
        else:
            print(row)
    print()

grid = {
    (i, j): list(range(1, 10))
    for i, row in enumerate(rows)
    for j, entry in enumerate(row)
    if entry == "."
}

aentries = []
for i in range(shape[0]):
    clue = []
    row = []
    for j in range(shape[1] + 1):
        if (i, j) in grid:
            clue.append((i, j))
        elif len(clue) > 0:
            if len(clue) > 1:
                row.append(clue)
            clue = []
    aentries.append(row)

dentries = []
for j in range(shape[1]):
    clue = []
    col = []
    for i in range(shape[0] + 1):
        if (i, j) in grid:
            clue.append((i, j))
        elif len(clue) > 0:
            if len(clue) > 1:
                col.append(clue)
            clue = []
    dentries.append(col)

for i, j in zip(aentries, aclues):
    assert len(i) == len(j)
for i, j in zip(dentries, dclues):
    assert len(i) == len(j)


changed = True
while changed:
    changed = False

    for N in range(max(shape)):
        for ii, jj in zip(aentries + dentries, aclues + dclues):
            for i, j in zip(ii, jj):
                if len(i) != N:
                    continue
                for a, b in enumerate(i):
                    if len(grid[b]) == 1:
                        for c, d in enumerate(i):
                            if a != c and grid[b][0] in grid[d]:
                                changed = True
                                grid[d].remove(grid[b][0])
                if j is not None:
                    valid = []
                    for option in product(*[grid[a] for a in i]):
                        if len(set(option)) == len(option) and sum(option) == j:
                            valid.append(option)
                    for a, b in enumerate(i):
                        for n in range(1, 10):
                            if n in grid[b] and n not in [v[a] for v in valid]:
                                grid[b].remove(n)
                                changed = True
    if changed:
        pretty_print(grid)

pretty_print(grid, True)

