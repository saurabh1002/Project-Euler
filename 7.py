# -*- coding: utf-8 -*-

# What is the 10 001st prime number?

from common_functions import check_prime, timing, PrimeSieve
    
timer = timing()

no_of_prime = 10001

prime = PrimeSieve(no_of_prime * 20)

nth_prime = prime[no_of_prime - 1]

timer("The 10001st prime number is {}".format(nth_prime))
