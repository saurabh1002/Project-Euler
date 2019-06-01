# -*- coding: utf-8 -*-

# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def factorial(num):
    fact = 1
    for i in xrange (1, num + 1):
        fact = fact * i
    return fact

num = factorial(100)
print num
sum = 0
while num !=0:
    sum = sum + (num % 10)
    num = (num - (num % 10))/10
print sum
