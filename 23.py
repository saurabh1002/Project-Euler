# -*- coding: utf-8 -*-

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from math import *

def sum_of_divisors(num):
    sum = 0
    i = 2
    while i <= sqrt(num):
        if (num % i == 0):
            if (i == (num / i)):
                sum = sum + i
            else:
                sum = sum + i + (num / i)
        i = i + 1

    return sum + 1

def check_abundant(num):
    if (sum_of_divisors(num) > num):
        return True
    else:
        return False

abundant_nos = []
for i in xrange (12, 28124):
    if (check_abundant(i)):
        abundant_nos.append(i)

list = []
for i in xrange (1, 28124):
    if (i % 2) == 0:
        if check_abundant(i / 2):
            continue
    list.append(i)

print list
sum = 0

for i in list[:]:
    print (len(list), 'len')
    flag = 0
    for j in abundant_nos:
        if (i - j) > 11 :
            if check_abundant(i - j):
                n = 1
                k = i
                while (k < 28124):
                    try:
                        # print (k, n, "k")
                        list.remove(k)
                        n = n + 1
                        k = i * n
                    except ValueError:
                        n = n + 1
                        k = i * n
                        # print("exception")
                        pass
                flag = 1
                break
        else:
            break
    if flag == 0:
        # print i
        sum = sum + i
        list.remove(i)

print sum
