# -*- coding: utf-8 -*-

# What is the 10 001st prime number?

from common_functions import check_prime, timing
    
timer = timing()

count = 4
num = 9
no_of_prime = 10001
while(count != no_of_prime):
    if(check_prime(num)):
        nth_prime = num
        count = count + 1

    if ((num % 10 == 1) or (num % 10 == 7) or (num % 10 == 9)):                  # Increment by 2 for decimal value other than 3
        num = num + 2
    else:
        num = num + 4

timer("The 10001st prime number is {}".format(nth_prime))
