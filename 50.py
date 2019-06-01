# -*- coding: utf-8 -*-

# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

list = [2]
for i in xrange (3, 1000000, 2):
    if (check_prime(i) == 1):
        list.append(i)

print len(list)

prev_p = 953

for i in xrange (3, len(list) / 4, 2):
    for j in xrange (0, len(list) - i):
        sum = 0
        for k in xrange (j, j + i):
            sum = sum + list[k]
            if sum > 1000000:
                break
        # print sum
        p = check_prime(sum)
        if (p == 1 and sum < 1000000):
            prev_p = sum
            print prev_p

print prev_p
