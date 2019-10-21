# -*- coding: utf-8 -*-

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

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
        multiply(v, i)

    # Find sum of digits in vector v[]
    num = np.array(v)
    return np.sum(num)


timer = timing()
n = 100
timer("Sum of the digits in the number 100! is {}".format(findSumOfDigits(n)))
