import random
import english

def distance(w, v):
    return len([i for i, j in zip(w, v) if i != j])

word = "WEIGHT"
word = "LODGE"

vowels = "AEIOU"

nearby = {i: [] for i in word}
for length in [5, 6, 7]:
    common = english.words(length)
    for w in english.words(length):
        n = [v for v in english.words(length, False) if distance(w, v) == 1]
        pos = {[num for num, (i, j) in enumerate(zip(w, v)) if i != j][0] for v in n}
        if len(pos) > 3 and len(n) > 15:
            olds = [[j for i, j in zip(w, v) if i != j][0] for v in n]
            news = [[j for i, j in zip(w, v) if i != j][0] for v in n]
            if all(i in news for i in word) and all(n[news.index(i)] in common for i in word):
                for i in word:
                    print(i, w, n[news.index(i)])
                    print()()
                print()
            for i, (old_l, new_l) in enumerate(zip(olds, news)):
                if new_l in word:
                    v = n[i]
                    if v in common:
                        nearby[new_l].append((w, v, n))

for letter, n in nearby.items():
    print(letter)
    for i in n:
        print(i)
    print()


# BETTER  LETTER  L
# LEVER   LOVER   O
# RIVER   RIDER   D
# STALE   STAGE   G
# WITHER  EITHER  E
