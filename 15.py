# -*- coding: utf-8 -*-

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

def factorial(num):
    fact = 1
    for i in xrange (1, num + 1):
        fact = fact * i
    return fact

grid_size = 20

ans = factorial(2 * grid_size)/(factorial(grid_size) ** 2)

print ans
