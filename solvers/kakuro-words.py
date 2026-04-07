from itertools import combinations
import english

# VIOLENT

abc = [i for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
for i in "VIOLENT":
    abc.remove(i)

tens = []

o = {}
for n in range(1, 10):
    o[n] = []
    for w1 in english.words(n):
        for i in w1:
            if w1.count(i) > 1:
                break
        else:
            o[n].append(w1)

for n in range(1, 5):
    print(n)
    for w1 in o[n]:
        print(w1)
        for w2 in o[10-n]:
            w = f"{w1} {w2}"
            for i in w:
                if w.count(i) > 1:
                    break
            else:
                for i in "VIOLENT":
                    if i not in w:
                        break
                else:
                    tens.append(w)

print(5)
for (n, w1) in enumerate(o[5]):
    print(w1)
    for w2 in o[5][:n]:
        w = f"{w1} {w2}"
        for i in w:
            if w.count(i) > 1:
                break
        else:
            for i in "VIOLENT":
                if i not in w:
                    break
            else:
                tens.append(w)

for w in english.words(10):
    for i in w:
        if w.count(i) > 1:
            break
    else:
        for i in "VIOLENT":
            if i not in w:
                break
        else:
            tens.append(w)


for a in combinations(abc, 3):
    letters = "VIOLENT" + "".join(a)
    long_words = []
    for word in tens:
        for i in word:
            if i not in letters + " ":
                break
        else:
            long_words.append(word)
    if len(long_words) == 0:
        continue
    words = []
    for w in english.words(7):
        for i in w:
            if w.count(i) > 1 or i not in letters:
                break
        else:
            words.append(w)
    if len(words) > 4:
        print(a, long_words)
        print(len(words))
        print(words)
        print()
