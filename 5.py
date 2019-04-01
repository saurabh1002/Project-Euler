# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
from math import sqrt

def highest_power_less_than_number(prime, number):
    a = 1
    while(a <= number):
        a = a * prime
    return a/prime

def check_prime(number):
    if (number == 2 or number == 3):
        return 1
    prime_flag = 1
    i = 2
    while (i <= sqrt(number)):
        if(number % i == 0):
            prime_flag = 0
            break
        i = i + 1
    if (prime_flag == 1):
        return 1

i = 2
ans = 1
number = 20
while (i <= number):
    is_prime = check_prime(i)
    if (is_prime):      # All primes greater than 5 have only these numbers in decimal place
        ans = ans * highest_power_less_than_number(i, number)
    i = i + 1

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is", ans)
