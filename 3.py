# -*- coding: utf-8 -*-

# What is the largest prime factor of the number 600851475143 ?

from common_functions import timing

timer = timing()

number = 600851475143
i = 3
global largest
largest = 1
while (i <= number):
    u =  i % 10
    if ((u == 1) or (u == 3) or (u == 7) or (u == 9)):      # All primes greater than 5 have only these numbers in decimal place
        while(number % i == 0):
            number = number / i                             # Divide by the prime factor to reduce computation
            if(i > largest):
                largest = i
    if ((u == 1) or (u == 7) or (u == 9)):                  # Increment by 2 for decimal value other than 3
        i = i + 2
    else:
        i = i + 4

timer("Largest Prime Factor is {}".format(largest))
