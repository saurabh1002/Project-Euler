# -*- coding: utf-8 -*-

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from common_functions import timing

timer = timing()

a = 1   # First Term of Fibonacci Sequence
b = 1   # Second Term of Fibonacci Sequence
c = 2
index = 3

while ((c % (10 ** 1000)) == (c % (10 ** 999))):

    a = b
    b = c
    c = a + b
    index = index + 1

timer("Index of the first term in the Fibonacci sequence to contain over 1000 digits is {}".format(index))
