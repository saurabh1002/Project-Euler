# -*- coding: utf-8 -*-

# Find the sum of all the primes below two million.
import numpy as np
from common_functions import timing, PrimeSieve

timer = timing()

prime_list = PrimeSieve(2000000)
sum = np.sum(prime_list)

timer("Sum of all primes below 2 million is {}".format(sum))
