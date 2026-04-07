import english

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

options = {i: [] for i in alphabet}


def works(letter, string, words, strict=True):
    #n = len([i for i in range(len(string) + 1) if string[:i] + letter + string[i:] not in words])
    #if strict:
    #    return n == 3
    #else:
    #    return n >= 3
    return letter + string in words and string + letter in words

    for i in range(len(string) + 1):
        if string[:i] + letter + string[i:] not in words:
            return False
    return True


for n in range(3, 15):
    words = english.words(n, False)

    for i in words:
        if works(i[0], i[1:], words):
            for j in alphabet:
                if j != i[0] and works(j, i[1:], words, False):
                    break
            else:
                options[i[0]].append(i)
                print(i)

for i, j in options.items():
    print(" ".join(j))


work = "EHDEEPSTT"
for n in range(3, 15):
    words = english.words(n, False)
    for w in words:
        for letter in w:
            if w.count(letter) > work.count(letter):
                break
        else:
            print(w)

D RAKE
E THOS
E ACH
R OUTE

DEER
WEIGHT

"""E WE
H AS
D AD
E AR
E AT
P AL
S IT
T EA
T EAS"""
