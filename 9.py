# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import *

for c in range (1, 500):
    a_plus_b = 1000.0 - c
    ab = ((a_plus_b ** 2.0) - (c ** 2.0)) * 0.5
    try:
        a = (a_plus_b + sqrt((a_plus_b ** 2.0) - (4 * ab))) / 2
        if a == int(a):
            b = ab / a
            print (a * b * c)

    except ValueError:
        pass
