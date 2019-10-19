# -*- coding: utf-8 -*-

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from common_functions import timing

def difference(n):
    sum_of_square = ((n * (n + 1) * ((2 * n) + 1)) / 6)
    square_of_sum = (((n * (n + 1)) * (n * (n + 1))) / 4)
    return square_of_sum - sum_of_square

timer = timing()

ans = difference(100)

timer("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {}".format(ans))
