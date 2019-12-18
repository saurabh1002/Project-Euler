# -*- coding: utf-8 -*-

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from math import *
from common_functions import check_prime, timing

timer = timing()

flag = True
odd_comp = 35
while (flag):
    if (not(check_prime(odd_comp))):
        GoldBach = False
        for i in range (3, odd_comp, 2):
            if (check_prime(i)):
                if (sqrt((odd_comp - i) / 2) == int(sqrt((odd_comp - i) / 2))):
                    GoldBach = True
        if (not GoldBach):
            flag = False

    odd_comp = odd_comp + 2

timer("The smallest odd number that does not satisfy Goldbach's conjecture is {}".format(odd_comp - 2))
