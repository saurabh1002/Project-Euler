# -*- coding: utf-8 -*-

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

from math import *

max_count = 0
p = 0
for i in xrange(12, 1000):
    count = 0
    for a in xrange(3, int(i / 4)):
        for b in xrange (a, int(i / 2)):
            if (a + b + sqrt(a ** 2 + b ** 2)) == i:
                count = count + 1
    if count > max_count:
        max_count = count
        p = i

print p
