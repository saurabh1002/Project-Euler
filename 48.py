# -*- coding: utf-8 -*-

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

sum = 0
for i in xrange (1, 1001):
    sum = sum + (i ** i)

num = 0
for i in xrange (0, 10):
    num = num + ((10 ** i) * (sum % 10))
    sum = (sum - (sum % 10)) / 10

print num
