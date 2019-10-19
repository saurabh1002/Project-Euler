# -*- coding: utf-8 -*-

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?
# from common_functions import timing
from math import *

# timer = timing()

num = 2 ** 1000
sum = 0
while num !=0:
    sum = sum + (num % 10)
    num = (num - (num % 10))/10

# timer("The sum of digits is {}".format(sum))
print (sum)