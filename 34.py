# -*- coding: utf-8 -*-

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import copy
from common_functions import timing, factorial

timer = timing()

total = 0
for i in range (11, 2540161):   # 9! * 7 = 2540160 is a seven digit number i.e. largest 7 digit number 9999999 has sum of factorial of its digits as 2540160 which is a seven digit number
    sum = 0
    j = copy.copy(i)
    while (j != 0):
        f = factorial(j % 10)
        sum = sum + f
        j = ((j - (j % 10)) / 10)
    if (sum == i):
        total = total + i

timer("sum of all numbers which are equal to the sum of the factorial of their digit is {}".format(total))
