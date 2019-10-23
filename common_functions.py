import time
import numpy as np
from math import *

def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

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


def PrimeSieve(n):
    """ Returns numpy array of all primes till n"""
    prime_list = []
    prime = np.ones((1, n+1))
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[0, p] == 1):
            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[0, i] = 0
        p += 1
    prime[0, 0] = 0
    prime[0, 1] = 0
    # append all prime numbers in a numpy array
    for p in range(n + 1):
        if prime[0, p]:
            prime_list.append(p)

    return np.array(prime_list)


def check_palindrome(num):
    integer = str(num)
    l = 0
    n = len(integer)-1
    if (integer[n] or integer[0]) == '0':
        return False
    while(n >= l):
        if(integer[l] != integer[n]):
            return False
        if l == n:
            return True
        l = l + 1
        n = n - 1
    return True


def number_of_divisors(num):
    count = 1
    if (num % 2 == 0):
        a = 0
        while (num % 2 == 0):
            num = num / 2
            a = a + 1
        count = count * (a + 1)

    while (num != 1):
        for i in range(3, int(num) + 1, 2):
            if (num == 1):
                break
            if (check_prime(i)):
                b = 0
                while (num % i == 0):
                    num = num / i
                    b = b + 1
                count = count * (b + 1)
    return count

def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * factorial(num - 1)


def sum_of_proper_divisors(num):
    sum = 1
    i = 2
    while i <= sqrt(num):
        if (num % i == 0):
            if (i == (num / i)):
                sum = sum + i
            else:
                sum = sum + i + (num / i)
        i = i + 1
    return sum


def dec_to_bin(num):
    list = ''
    while(num != 0):
        if (num % 2) == 0:
            list = '0' + list
            num = num / 2
        if (num % 2) == 1:
            list = '1' + list
            num = (num - 1) / 2
    return int(list)
