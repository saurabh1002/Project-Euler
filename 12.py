# -*- coding: utf-8 -*-

# What is the value of the first triangle number to have over five hundred divisors?
from common_functions import number_of_divisors, timing

def triangle_num(i):
    triangle_number = i * (i + 1) * 0.5
    return triangle_number

timer = timing()

largest_count = 1
n = 100
while (largest_count <= 500):
    tri_num = triangle_num(n)
    largest_count = number_of_divisors(tri_num)
    n = n + 1

timer("{} is the first triangle number to have over 500 divisors".format(tri_num))
