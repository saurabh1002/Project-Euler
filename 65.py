# -*- coding: utf-8 -*-

# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

def sum_of_digits(num):
    sum = 0
    while (num != 0):
        sum = sum + (num % 10)
        num = (num - (num % 10)) / 10
    return sum

def calc_frac(a, b, c):
    return ((a * c) + b), c

def nth_convergent(n):
    count = 1
    seq = [1]
    n = n-1
    while n != 0:
        seq.append(2 * count)
        count = count + 1
        n = n - 1
        if n != 0:
            seq.append(1)
            n = n - 1
        if n != 0:
            seq.append(1)
            n = n - 1
    print seq

    c = seq.pop()
    a = seq.pop()
    b = 1
    den, num = calc_frac(a, b, c)

    while len(seq) != 0:
        a = seq.pop()
        b = num
        c = den
        den, num = calc_frac(a, b, c)

    num, den = calc_frac (2, num, den)
    print num, den
    print sum_of_digits(num)

n = input("Enter value of n for the nth convergent fractions numerators sum: ")
nth_convergent(n - 1)