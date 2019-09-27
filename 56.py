# -*- coding: utf-8 -*-

# A googol(10^100) is a massive number: one followed by one-hundred zeros
# 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

def digital_sum(num):
    sum_ = 0
    while (num != 0):
        sum_ = sum_ + (num % 10)
        num = (num - (num % 10)) / 10
    return sum_

larger_sum = 0
for i in xrange(2, 100):
    if i % 10 == 0:
        continue
    for j in xrange(2, 100):
        num = i ** j
        total = digital_sum(num)
        if total > larger_sum:
            larger_sum = total

print larger_sum