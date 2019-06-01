# -*- coding: utf-8 -*-
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

def total(a, b, c, d, e, f, g, h):
    val = 200 * a + 100 * b + 50 * c + 20 * d + 10 * e + 5 * f + 2 * g + h
    if val == 200:
        return True
    else:
        return False

count = 0
for h in xrange (0, 201):
    for g in xrange (0, 101):
        if (h + 2 * g) > 200:
            continue
        for f in xrange (0, 41):
            if (h + 2 * g + 5 * f) > 200:
                continue
            for e in xrange (0, 21):
                if (h + 2 * g + 5 * f + 10 * e) > 200:
                    continue
                for d in xrange (0, 11):
                    if (h + 2 * g + 5 * f + 10 * e + 20 * d) > 200:
                        continue
                    for c in xrange (0, 5):
                        if (h + 2 * g + 5 * f + 10 * e + 20 * d + 50 * c) > 200:
                            continue
                        for b in xrange (0, 3):
                            if (h + 2 * g + 5 * f + 10 * e + 20 * d + 50 * c + 100 * b) > 200:
                                continue
                            for a in xrange (0, 2):
                                if total(a, b, c, d, e, f, g, h) == True:
                                    print (a, b, c, d, e, f, g, h)
                                    count = count + 1
print count
