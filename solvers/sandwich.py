import english

words2 = english.words(2, common=False)
words3 = english.words(3, common=False)
words4 = english.words(4, common=False)
words5 = english.words(5, common=False)
words6 = english.words(6, common=False)
words7 = english.words(7, common=False)
words8 = english.words(8, common=False)
words9 = english.words(9, common=False)

for a, z in [
    ("G", "W"),
    ("O", "O"),
    ("O", "R"),
    ("D", "K"),
]:
    print(a, z)
    for short, long in [(words2, words4), (words3, words5), (words4, words6), (words5, words7), (words6, words8), (words7, words9)]:
        for w in short:
            if f"{a}{w}{z}" in long:
                print(w)
    print()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
long = english.words(common=False)

for clues in [
    ["LO", "RO", "NA"],
    ["NT", "RZ", "REGAN"],
    ["THE", "RANGE", "VE"],
    ["UC", "RUN", "ES"]
]:
    options = []
    for a in alphabet:
        for z in alphabet:
            for c in clues:
                if f"{a}{c}{z}" not in long:
                    break
            else:
                options.append((a, z))
    print(clues, options)
