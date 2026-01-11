import english

colours = [
    "RED", "GREEN", "BLUE", "ORANGE", "PINK", "SCARLET", "MAGENTA", "PURPLE", "WHITE", "BLACK",
    "BROWN", "GOLD", "SILVER", "CYAN", "YELLOW", "CRIMSON", "INDIGO", "VIOLET", "MAROON", "GREY",
    "CREAM", "SEPIA", "BRONZE", "SALMON", "COPPER", "TEAL", "BEIGE", "LILAC", "MAUVE", "BURGUNDY",
    "OCHRE",
]

for c in colours:
    started = False
    for w in english.words(len(c) + 1, common=False):
        for i in c:
            if c.count(i) > w.count(i):
                break
        else:
           for i in w:
                if w.count(i) > c.count(i) and i == "N":
                    if not started:
                        print(f"# {c}")
                        started = True
                        print(w, i)
                    break
    if started:
        print()


# CYAN
# C + 
# Y + GREEN = ENERGY
# A + RED = DEAR
# N + VIOLET = VIOLENT

# GREY
# G + WHITE = WEIGHT
# R + SEPIA = PRAISE
# E + GOLD = LODGE
# Y + GREEN = ENERGY

# GREEN
# G + WHITE = WEIGHT
# R + TEAL = ALERT
# E + RED = DEER
# E + GOLD = LODGE
# N + VIOLENT = VIOLENT
#
# # RESERVE
# R + SEPIA = PRAISE
# E + SCARLET = CLEAREST
