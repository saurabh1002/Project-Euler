# -*- coding: utf-8 -*-

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either(i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers
# the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

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

def reverse_number(num):
    rev = 0
    while(num != 0):
        rev = rev + num % 10
        rev = rev * 10
        num = (num - (num % 10)) / 10
    return rev/10

def check_lychrel(num):
    count = 0
    while (count < 50):
        num = num + reverse_number(num)
        if (check_palindrome(num) == False):
            count = count + 1
        else:
            return False
    return True

count = 0
for i in xrange(1, 10000):
    if check_lychrel(i):
        count = count + 1
print count
