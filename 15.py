# -*- coding: utf-8 -*-

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

from common_functions import timing, factorial

timer = timing()

grid_size = 20

ans = factorial(2 * grid_size)/(factorial(grid_size) ** 2)

timer("There are {} routes through the 20x20 grid".format(ans))
