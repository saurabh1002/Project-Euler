# -*- coding: utf-8 -*-

# Euler discovered the remarkable quadratic formula:
#
# n^2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

from math import *
from common_functions import timing, check_prime, PrimeSieve

timer = timing()
b = PrimeSieve(1000)

a_b = []
for i in range (-999, 1000, 1):
    for j in b:
        if (((i + j + 1) > 0) and (check_prime(i + j + 1))):
            a_b.append([i,j])

n = 0
while(len(a_b) != 1):
    for ab in a_b[:]:
        if len(a_b) != 1:
            if (((n ** 2) + (ab[0] * n) + ab[1]) <= 0):
                a_b.remove(ab)
                continue
            val = check_prime(((n ** 2) + (ab[0] * n) + ab[1]))
            if (val != 1):
                a_b.remove(ab)
    n = n + 1

timer("The product of the coefficients is {}".format(a_b[0][0] * a_b[0][1]))
