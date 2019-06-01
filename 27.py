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

def check_prime(number):
    if (number == 1):
        return False
    if (number == 2 or number == 3):
        return True
    i = 2
    while (i <= sqrt(number)):
        if(number % i == 0):
            return False
        i = i + 1
    return True

b = [2, 3]

for i in xrange (5, 1000, 2):
    if (check_prime(i)):
        b.append(i)
print b

a_b = []
for i in xrange (-999, 1000, 1):
    for j in b:
        if (((i + j + 1) > 0) and (check_prime(i + j + 1))):
            a_b.append([i,j])

print len(a_b)

n = 0
while(len(a_b) != 1):
    for ab in a_b[:]:
        if len(a_b) != 1:
            if (((n ** 2) + (ab[0] * n) + ab[1]) <= 0):
                print('1')
                a_b.remove(ab)
                continue
            val = check_prime(((n ** 2) + (ab[0] * n) + ab[1]))
            if (val != 1):
                print('2')
                a_b.remove(ab)
        print(len(a_b))
    n = n + 1
print a_b[0][0] * a_b[0][1]
