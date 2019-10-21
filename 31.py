# -*- coding: utf-8 -*-
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
from common_functions import timing

def total(a, b, c, d, e, f, g, h):
    val = 200 * a + 100 * b + 50 * c + 20 * d + 10 * e + 5 * f + 2 * g + h
    if val == 200:
        return True
    else:
        return False

timer = timing()
count = 0
for a in range (0, 2):
    for b in range (0, 3):
        if (200 * a + 100 * b) > 200:
            break
        for c in range (0, 5):
            if (200 * a + 100 * b + 50 * c) > 200:
                break
            for d in range (0, 11):
                if (200 * a + 100 * b + 50 * c + 20 * d) > 200:
                    break
                for e in range (0, 21):
                    if (200 * a + 100 * b + 50 * c + 20 * d + 10 * e) > 200:
                        break
                    for f in range (0, 41):
                        if (200 * a + 100 * b + 50 * c + 20 * d + 10 * e + 5 * f) > 200:
                            break
                        for g in range (0, 101):
                            if (200 * a + 100 * b + 50 * c + 20 * d + 10 * e + 5 * f + 2 * g) > 200:
                                break
                            for h in range (0, 201):
                                if total(a, b, c, d, e, f, g, h):
                                    count = count + 1
timer("$2 can be made in {} ways using any number of coins".format(count))
