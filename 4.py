# -*- coding: utf-8 -*-

# What is the largest Palindrome which is a product of two 3 digit numbers?

from common_functions import check_palindrome, timing

timer = timing()

largest_pal = 0
for a in range (999, 99, -1):
    for b in range(999, 99, -1):
        if (a != b):
            if (a*b < largest_pal):
                break
            if(check_palindrome(a*b)):
                if(largest_pal <= a*b):
                    largest_pal = a*b
                break

timer("The largest Palindrome which is a product of two 3 digit numbers is {}".format(largest_pal))
