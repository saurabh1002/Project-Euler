# -*- coding: utf-8 -*-

# Find the sum of all the primes below two million.

from math import sqrt

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

sum = 17
num = 9

while(num < 2000000):
#    print (num)
    if(check_prime(num)):
        sum = sum + num

    if ((num % 10 == 1) or (num % 10 == 7) or (num % 10 == 9)):                  # Increment by 2 for decimal value other than 3
        num = num + 2
    else:
        num = num + 4

print(sum)
