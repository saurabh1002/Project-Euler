# Find the sum of all the primes below two million.

from math import sqrt

def check_prime(number):
    if (number == 2 or number == 3):
        return 1

    prime_flag = 1
    i = 3
    while (i <= sqrt(number)):

        if(number % i == 0):
            prime_flag = 0
            break                             # Divide by the prime factor to reduce computation

        i = i + 2

    if (prime_flag == 1):
        return 1

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
