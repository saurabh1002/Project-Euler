# -*- coding: utf-8 -*-

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

def no_of_digits(num):
    count = 0
    while (num != 0):
        num = (num - (num % 10)) / 10
        count = count + 1
    return count

def is_num_greater(num, den):
    if no_of_digits(num) > no_of_digits(den):
        return True
    else:
        return False

def calc_frac(a, b, c):
    return ((a * c) + b), c

def cont_frac(i):
    num = 1
    den = 2
    while (i != 1):
        den, num = calc_frac(2, num, den)
        i = i - 1
    num, den = calc_frac(1, num, den)
    return num, den

count = 0
for i in xrange(1, 1001):
    num, den = cont_frac(i)
    if is_num_greater(num, den):
        count = count + 1

print count




