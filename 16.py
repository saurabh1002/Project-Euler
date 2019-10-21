# -*- coding: utf-8 -*-

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
# from common_functions import timing
from common_functions import timing
import numpy as np


def multiply(v, x):
    carry = 0
    size = len(v)
    for i in range(size):
        # Calculate res + prev carry
        res = carry + v[i] * x
        # updation at ith position
        v[i] = res % 10
        carry = res // 10
    while (carry != 0):
        v.append(carry % 10)
        carry //= 10

# Returns sum of digits in n!
def findSumOfDigits(n):
    v = [1]
    for i in range(1, n + 1):
        multiply(v, 2)

    # Find sum of digits in vector v[]
    num = np.array(v)
    return np.sum(num)


timer = timing()
n = 1000
timer("Sum of the digits in the number 2^1000 is {}".format(findSumOfDigits(n)))
