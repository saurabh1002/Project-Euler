# -*- coding: utf-8 -*-

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from common_functions import check_palindrome, timing, dec_to_bin
import numpy as np 

timer = timing()

list = []
for i in range (1, 1000000):
    if (check_palindrome(i)):
        list.append(i)
arr = np.array(list)

sum = 0
for a in arr:
    bin = dec_to_bin(a)
    if check_palindrome(bin):
        sum = sum + a

timer("The sum of all numbers, less than one million, which are palindromic in base 10 and base 2 is {}".format(sum))
