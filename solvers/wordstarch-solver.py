import random
import english
import matplotlib.pylab as plt

def distance(w, v):
    return len([i for i, j in zip(w, v) if i != j])

grid = [
    ['S', 'N', 'A', 'R', 'E', 'V', 'O', 'L'],
    ['P', 'R', 'E', 'W', 'S', 'N', 'A', 'E'],
    ['D', 'L', 'O', 'T', 'P', 'L', 'O', 'T'],
    ['L', 'O', 'A', 'D', 'A', 'G', 'E', 'T'],
    ['A', 'G', 'E', 'N', 'C', 'Y', 'B', 'E'],
    ['E', 'I', 'T', 'H', 'E', 'R', 'U', 'R'],
    ['C', 'U', 'R', 'E', 'D', 'I', 'R', 'E'],
    ['G', 'N', 'I', 'T', 'T', 'I', 'N', 'K'],
]

words = sorted(['STALE', 'RIVER', 'BETTER', 'LEVER', 'WITHER', 'PACED', 'CURED', 'AGENCY', 'PLOT', 'KNITTING', 'SNARE', 'PLANE', 'TOLD', 'DIRE',
         'BURN', 'ANSWER'])

plt.plot([-0.5,7.5,7.5,-0.5,-0.5], [-0.5, -0.5, 7.5, 7.5, -0.5], "k-")
for i, row in enumerate(grid):
    for j, letter in enumerate(row):
        plt.text(j, 7-i, letter, va="center", ha="center")

lines = {}
for i, r in enumerate(grid):
    lines[f"row {i}"] =  (
        "".join(r),
        [(i, j) for j, _ in enumerate(r)]
    )
for i, c in enumerate(grid[0]):
    lines[f"col {i}"]  = (
        "".join(r[i] for r in grid),
        [(j, i) for j, _ in enumerate(grid)],
    )
for i in range(-7, 8):
    lines[f"bdiag {i}"] = (
        "".join(row[i+j] for j, row in enumerate(grid) if 0 <= i + j < len(row)),
        [(j, i+j) for j, row in enumerate(grid) if 0 <= i + j < len(row)],
    )
for i in range(15):
    lines[f"fdiag {i}"] = (
        "".join(row[i-j] for j, row in enumerate(grid) if 0 <= i - j < len(row)),
        [(j, i-j) for j, row in enumerate(grid) if 0 <= i - j < len(row)],
    )

for w in words:
    found = []
    for where, (f_line, f_coords) in lines.items():
        for line, coords in [(f_line, f_coords), (f_line[::-1], f_coords[::-1])]:
            for i in range(len(line) + 1 - len(w)):
                string = line[i:i+len(w)]
                c = coords[i:i+len(w)]
                if w == string:
                    # print(where, string)
                    found.append((where, i, c))
                if distance(w, string) == 1:
                    if string in english.words(len(w), False):
                        # print(where, string)
                        found.append((where, i, c, string))
                    else:
                        pass
                        print(where, string, "x")
    if len(found) == 1:
        if len(found[0]) == 3:
            print(w)
        else:
            print(w, found[0][3], [j for i, j in zip(w, found[0][3]) if i != j][0])
        print("",
            [found[0][2][0][0], found[0][2][-1][0]],
            [7-found[0][2][0][1], 7-found[0][2][-1][1]],
        )
        plt.plot(
            [found[0][2][0][1], found[0][2][-1][1]],
            [7-found[0][2][0][0], 7-found[0][2][-1][0]],
            "-",
        )
    else:
        print(f"TODO: {w}")
        for i in found:
            print("", *i)

plt.axis("equal")
plt.show()
