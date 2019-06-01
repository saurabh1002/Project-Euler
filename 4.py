# -*- coding: utf-8 -*-

# What is the largest Palindrome which is a product of two 3 digit numbers?
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

largest_pal = 0
for a in xrange (100, 1000, 1):
    for b in xrange(100, 1000, 1):
        if (a != b):
            if(check_palindrome(a*b)):
                if(largest_pal <= a*b):
                    largest_pal = a*b
                    num1 = a
                    num2 = b

print(largest_pal, num1, num2)
