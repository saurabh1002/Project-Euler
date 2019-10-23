# -*- coding: utf-8 -*-

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from common_functions import timing

def remove_common(a, b):
    i = a % 10.0
    j = (a - (a % 10.0)) / 10.0
    k = b % 10
    l = (b - (b % 10.0)) / 10.0

    try:
        if (i == 0.0 and k == 0.0):
            return -1
        elif ( i == k):
            return j / l
        elif (i == l):
            return j / k
        elif (j == k):
            return i / l
        elif (j == l):
            return i / k
        else:
            return -1
    except ZeroDivisionError:
        return -1


timer = timing()

num = 1.0
den = 1.0
for i in range (10, 100):
    for j in range (10, 100):
        if i < j:
            num_1 = float(i) / float(j)
            num_2 = remove_common(float(i), float(j))
            if (num_1 == num_2):
                num = num * i
                den = den * j

for i in range (2, int(num / 2)):
    while(num % i == 0 and den % i == 0):
        num = num / i
        den = den / i

timer("The value of the denominator is {}".format(den))
