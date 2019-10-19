# -*- coding: utf-8 -*-

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
from common_functions import check_prime, timing

def highest_power_less_than_number(prime, number):
    a = 1
    while(a <= number):
        a = a * prime
    return a/prime

timer = timing()

i = 2
ans = 1
number = 20
while (i <= number):
    is_prime = check_prime(i)
    if (is_prime):      # All primes greater than 5 have only these numbers in decimal place
        ans = ans * highest_power_less_than_number(i, number)
    i = i + 1

timer("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}".format(ans))
