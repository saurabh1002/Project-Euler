# -*- coding: utf-8 -*-

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from math import *
from common_functions import timing, sum_of_proper_divisors
import numpy as np

def check_abundant(num):
    if (sum_of_proper_divisors(num) > num):
        return True
    else:
        return False

temp = []
for i in range (12, 28124):
    if (check_abundant(i)):
        temp.append(i)
abundant_nos = np.array(temp)

list = []
for i in range (1, 28124):
    if (i % 2) == 0:
        if check_abundant(i / 2):
            continue
    list.append(i)

sum = 0
for i in list[:]:
    flag = 0
    for j in abundant_nos:
        if (i - j) > 11 :
            if check_abundant(i - j):
                n = 1
                k = i
                while (k < 28124):
                    try:
                        list.remove(k)
                        n = n + 1
                        k = i * n
                    except ValueError:
                        n = n + 1
                        k = i * n
                        pass
                flag = 1
                break
        else:
            break
    if flag == 0:
        sum = sum + i
        list.remove(i)

print(sum)
