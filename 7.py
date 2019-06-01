# -*- coding: utf-8 -*-

# What is the 10 001st prime number?

from math import *

def check_prime(number):
    if (number == 1):
        return False
    if (number == 2 or number == 3):
        return True
    i = 2
    while (i <= sqrt(number)):
        if(number % i == 0):
            return False
        i = i + 1
    return True
    
count = 4
num = 9
no_of_prime = 10001
while(count != no_of_prime):
#    print (num)
    if(check_prime(num)):
        nth_prime = num
        count = count + 1

    if ((num % 10 == 1) or (num % 10 == 7) or (num % 10 == 9)):                  # Increment by 2 for decimal value other than 3
        num = num + 2
    else:
        num = num + 4

print(nth_prime)
