# -*- coding: utf-8 -*-

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime
# that is, a ratio of 8/13 ≈ 62 % .

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

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

size = 3
no_of_diag = 5.0
count = 0.0
n = 1
ratio = 1.0

while ratio >= 0.1:

    a = ((size - 1) ** 2) + 1
    b = a + size - 1
    c = (size ** 2) - (6 * n)

    if check_prime(a):
        count = count + 1.0
    if check_prime(b):
        count = count + 1.0
    if check_prime(c):
        count = count + 1.0

    ratio = count / no_of_diag

    print (a, b, c, ratio)

    no_of_diag = no_of_diag + 4.0
    size = size + 2
    n = n + 1

print (size - 2)
