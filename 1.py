# -*- coding: utf-8 -*-

# Find the sum of all the multiples of 3 or 5 below 1000.

from common_functions import timing

timer = timing()

sum = 0
for i in range (1, 1000, 1):    # Loop through all natural numbers below 1000
    if ((i % 3 == 0) or (i % 5 == 0)): # Check for divisilbility by 3 or 5
        sum = sum + i

timer("The sum of all natural numbers below 1000, divisible by 3 or 5 is = {}".format(sum))
