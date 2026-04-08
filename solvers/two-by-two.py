from itertools import combinations
import english

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for sol in ["ALERT", "LODGE", "WEIGHT"]:
    print(sol, "A")
    for w in english.words(5, False):
        if w[1] == sol[0] and w[2] == sol[3] and w[3] == sol[4] and (len(sol) == 5 or w[4] == sol[5]):
            print("", w)
    print("".join(" " for _ in sol), "D")
    for w in english.words(5, False):
        if w[1] == sol[1] and w[4] == sol[1]:
            print("", w)


best = [None, []]

for sol in ["ALERT", "LODGE", "WEIGHT"]:
    for i in combinations(alphabet, 10-len(sol)):
        letters = sol + "".join(i)
        if len({j for j in letters}) != 10:
            continue
        words = []
        for w in english.words(len(sol), False):
            for l in w:
                if w.count(l) > letters.count(l):
                    break
            else:
                words.append(w)
        if len(words) > 400:
            matches = [w for w in words if w[1] == sol[0] and w[2] == sol[3] and w[3] == sol[4] and (
                len(sol) == 5 or w[4] == sol[5]
            )]
            if len(matches) > 0 and "PARTY" in matches:
                print(letters, len(words))
                print()
                print(" ".join(matches))
                print()
                print(" ".join(words))
                print()
                print()
        if len(words) > len(best[1]):
            best = [letters, words]

print()
print(best[0], len(best[1]))
print(" ".join(best[1]))
