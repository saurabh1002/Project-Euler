# -*- coding: utf-8 -*-

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

from common_functions import timing

timer = timing()

a = 1   # First Term of Fibonacci Sequence
b = 2   # Second Term of Fibonacci Sequence
c = 3   # Third Term of Fibonacci Sequence
sum = 2 # Sum of even terms

while (c < 4000000):
    if (c % 2 == 0):    # Check for even number
        sum = sum + c
    a = b
    b = c
    c = a + b

timer("The sum of even-valued terms of a Fibonacci Sequence below four million is = {}".format(sum))
