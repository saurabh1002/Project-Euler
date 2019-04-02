# What is the value of the first triangle number to have over five hundred divisors?
from math import sqrt

largest_count = 1

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

def find_divisor_num(num):
    count = 1
    if (num % 2 == 0):
        a = 0
        while (num % 2 == 0):
            num = num / 2
            a = a + 1
        count = count * (a + 1)

    while (num != 1):
        for i in range (3, int(num) + 1, 2):
            if (num == 1):
                break
            if (check_prime(i)):
                b = 0
                while (num % i == 0):
                    num = num / i
                    b = b + 1
                count = count * (b + 1)
            # print (i, num, count)

    return count

def triangle_num(i):
    triangle_number = i * (i + 1) * 0.5
    return triangle_number

nth = 10
while (largest_count <= 500):
    tri_num = triangle_num(nth)
    largest_count = find_divisor_num(tri_num)
    nth = nth + 1
    print (largest_count, tri_num)
