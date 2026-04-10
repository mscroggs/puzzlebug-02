import english

poss = {i: [] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
poss2 = {i: [] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

for n in [
    "ZERO",
    "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN",
    "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN",
    "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY",
]:
    for i, letter in enumerate(n):
        w = n[:i] + n[i+1:]
        if w in english.words(len(w)):
            poss[letter].append(w)
            print(letter, w)
        elif w in english.words(len(w), False):
            poss2[letter].append(w)
            print("(", letter, w, ")")

print()

for i in "NICEWORK":
    if len(poss[i]) == 0:
        print(i, poss[i], poss2[i])
    else:
        print(i, poss[i])

print()

for i, p in poss.items():
    if len(p) > 0:
        print(i, p)
    elif len(poss2[i]) > 0:
        print(i, poss2[i])
