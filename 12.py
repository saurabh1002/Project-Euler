# -*- coding: utf-8 -*-

# What is the value of the first triangle number to have over five hundred divisors?
from common_functions import number_of_divisors, timing

triangle_number = lambda i: i * (i + 1) * 0.5

timer = timing()

largest_count = 1
n = 100
while (largest_count <= 500):
    tri_num = triangle_number(n)
    largest_count = number_of_divisors(tri_num)
    n = n + 1

timer("{} is the first triangle number to have over 500 divisors".format(tri_num))
