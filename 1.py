# -*- coding: utf-8 -*-

# Find the sum of all the multiples of 3 or 5 below 1000.

from common_functions import timing
import functools as ft

timer = timing()

f = lambda s,a: s+a if ((a % 3 == 0) or (a % 5 == 0)) else s
sum = ft.reduce(f, range(0, 1000))

timer("The sum of all natural numbers below 1000, divisible by 3 or 5 is = {}".format(sum))
