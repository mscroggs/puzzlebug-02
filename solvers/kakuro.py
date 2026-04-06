from random import shuffle, seed
from itertools import product, permutations

seed(3)

RED = "\033[31m"
DEFAULT = "\033[0m"


def pretty_print(grid, show_options=False):
    for i in range(shape[0]):
        row = "".join((f"{grid[(i, j)][0]}" if len(grid[(i, j)]) == 1 else f"{RED}{len(grid[(i, j)])}{DEFAULT}") if (i, j) in grid else "#" for j in range(shape[1]))
        if show_options:
            print(row, *["[...]" if len(grid[(i, j)]) > 5 else grid[(i, j)] for j in range(shape[1]) if (i, j) in grid])
        else:
            print(row)
    print()


def solve(rows, aclues, dclues, printing=False):
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
        if changed and printing:
            pretty_print(grid)

    if printing:
        pretty_print(grid, True)

    return grid


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

sol = solve(rows, aclues, dclues, True)

word = [i for i in "COUNTLIVES"]

code = {}

for i, l in enumerate("VIOLENT"):
    code[sol[(0,i + 2)][0]] = l
    word.remove(l)

shuffle(word)

for i in range(10):
    if i not in code:
        code[i] = word.pop()

print(code)

for i in range(shape[0]):
    row = "".join(code[sol[(i, j)][0]] if (i, j) in sol else "#" for j in range(shape[1]))
    print(row)
print()


acodes = [
    ["".join(code[int(i)] for i in str(j)) for j in c]
    for c in aclues
]
dcodes = [
    ["".join(code[int(i)] for i in str(j)) for j in c]
    for c in dclues
]

print("ACLUES")
for c in aclues:
    print(["".join(code[int(i)] for i in str(j)) for j in c])
print("DCLUES")
for c in dclues:
    print(["".join(code[int(i)] for i in str(j)) for j in c])

preamble = True

lines = []
if preamble:
    lines.append("\\documentclass{standalone}")
    lines.append("\\usepackage{tikz}")
    lines.append("\\usepackage{fontspec}")
    lines.append("\\setmainfont{Bubble Sans}")
    lines.append("\\begin{document}")
lines.append("\\begin{tikzpicture}")

lines.append(f"\\fill[white] (-1,0) rectangle +({shape[1] + 1},{shape[0] + 1});")
lines.append("\\fill[black] " + (
    " ".join(f"(-1,{i}) rectangle +(1,1)" for i in range(0, shape[0] + 1))
) + (
    " ".join(f"({i},{shape[0]}) rectangle +(1,1)" for i in range(shape[1]))
) + (
    " ".join(f"({j},{shape[0] - 1 - i}) rectangle +(1,1)" for i in range(shape[1]) for j in range(shape[0]) if (i,j) not in sol)
) + ";")

for i, c in enumerate(acodes):
    n = 0
    for j in range(shape[1]):
        if (i, j-1) not in sol and (i, j) in sol and (i, j+1) in sol:
            lines.append(f"\\fill[black!20!white] ({j},{shape[0] - i-1}) -- +(0,1) -- +(-1,1) -- cycle;")
            lines.append(f"\\node[inner sep=2pt,anchor=east] at ({j},{shape[0] - i-1}.7) {{{c[n]}}};")
            n += 1

for j, c in enumerate(dcodes):
    n = 0
    for i in range(shape[0]):
        if (i-1, j) not in sol and (i, j) in sol and (i+1, j) in sol:
            lines.append(f"\\fill[black!20!white] ({j},{shape[0] - i}) -- +(1,0) -- +(0,1) -- cycle;")
            lines.append(f"\\node[inner sep=2pt,anchor=south] at ({j}.3,{shape[0] - i}) {{{c[n]}}};")
            n += 1

lines.append(f"\\foreach \\x in {{-1,...,{shape[1]}}}")
lines.append(f"  \\draw (\\x,0) -- (\\x,{shape[0] + 1});")
lines.append(f"\\foreach \\y in {{0,...,{shape[0] + 1}}}")
lines.append(f"  \\draw (-1,\\y) -- ({shape[1]},\\y);")

lines.append("\\draw " + (
    " ".join(f"({i},{shape[0]+1}) -- +(1,-1)" for i in range(shape[1]))
) + (
    " ".join(f"({j},{shape[0] - i}) -- +(1,-1)" for i in range(shape[1]) for j in range(shape[0]) if (i,j) not in sol)
) + ";")

for i, j in [
    (3,5), (4,3), (5,6), (6,4)
]:
    lines.append(f"\\node[black!50!white] at ({j}.5,{shape[0] - 1 - i}.5) {{\\large {code[sol[(i, j)][0]]}}};")

lines.append("\\end{tikzpicture}")
if preamble:
    lines.append("\\end{document}")

with open("kakuro.tex", "w") as f:
    f.write("\n".join(lines))

print()()



start = -1

all_sols = []

for p in permutations(range(10)):
    def replace(n):
        if p[int(str(n)[0])] == 0:
            raise ValueError
        return int("".join(
            str(p[int(i)]) for i in str(n)
        ))
    try:
        new_aclues = [[replace(j) for j in i] for i in aclues]
        new_dclues = [[replace(j) for j in i] for i in dclues]
    except ValueError:
        continue
    print(p, len(all_sols))
    solutions = solve(rows, new_aclues, new_dclues)
    nsols = 1
    for i in solutions.values():
        nsols *= len(i)
    if nsols > 0:
        pretty_print(solutions, True)
        all_sols.append(solutions)

print(len(all_sols), "solutions")
