# -*- coding: utf-8 -*-

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import copy

def factorial(num):
    fact = 1
    for i in xrange (1, num + 1):
        fact = fact * i
    return fact

total = 0

for i in xrange (11, 2540161):
    print i
    sum = 0
    j = copy.copy(i)
    while (j != 0):
        sum = sum + (factorial(j % 10))
        j = ((j - (j % 10)) / 10)
    if (sum == i):
        total = total + i

print total
