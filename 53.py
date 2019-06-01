# -*- coding: utf-8 -*-

# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3=10.
#
# In general, nCr=n! / r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
#
# It is not until n=23, that a value exceeds one-million: 23C10=1144066.
#
# How many, not necessarily distinct, values of nCr for 1≤n≤100, are greater than one-million?

def factorial(num):
    fact = 1
    for i in xrange (1, num + 1):
        fact = fact * i
    return fact

def nCr(n, r):
    return (factorial(n) / (factorial(n - r) * factorial(r)))

count = 0
for n in xrange (23, 101):
    for r in xrange (3, (int(n/2) + 1)):
        if nCr(n, r) > 1000000:
            if r == n - r:
                count = count + 1
            else:
                count = count + 2
print count
