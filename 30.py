# -*- coding: utf-8 -*-

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import copy
from common_functions import timing

timer = timing()

total = 0
for i in range (100, 1000000):
    sum = 0
    j = copy.copy(i)
    while(j != 0):
        sum = sum + ((j % 10) ** 5)
        j = (j - (j % 10)) / 10
    if (sum == i):
        total = total + i
timer("Sum of all numbers that can be written as sum of fifth powers of their digits is {}".format(total))
