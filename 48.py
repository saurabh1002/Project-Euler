# -*- coding: utf-8 -*-

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
from common_functions import timing

timer = timing()
sum = 0
for i in range (1, 1001):
    sum = sum + (i ** i)

num = 0
for i in range (0, 10):
    num = num + ((10 ** i) * (sum % 10))
    sum = (sum - (sum % 10)) / 10

timer("The last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000 are {}".format(num))
