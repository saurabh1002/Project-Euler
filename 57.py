# -*- coding: utf-8 -*-

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
import time

calc_frac = lambda a,b,c:(a*c)+b

def cont_frac(i, num, den):
    global num_p, den_p

    den_p, num_p = calc_frac(2, num, den), den
    num_r, den_r = calc_frac(1, num_p, den_p), den_p

    return num_r, den_r

start_time = time.time()

num_p = 1
den_p = 2

count = 0
for i in range(2, 1001):
    num, den = cont_frac(i, num_p, den_p)
    if len(str(num)) > len(str(den)):
        count += 1

print(time.time() - start_time)
print count



