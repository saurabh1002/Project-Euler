# -*- coding: utf-8 -*-

# Consider quadratic Diophantine equations of the form:

# x2 – Dy2 = 1

# For example, when D = 13, the minimal solution in x is 6492 – 13×1802 = 1.

# It can be assumed that there are no solutions in positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

# 32 – 2×22 = 1
# 22 – 3×12 = 1
# 92 – 5×42 = 1
# 52 – 6×22 = 1
# 82 – 7×32 = 1

# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D = 5.

# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


from math import sqrt
import copy

def check_square(num):
    if int(sqrt(num)) == sqrt(num):
        return True
    else:
        return False

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

list = []
x_old = 0.0
d = 0.0

for i in xrange(2, 1001):
    if check_square(i):
        continue
    list.append(float(i))

for i in list:
    # input()
    print (i)    
    x_sq_minus_1 = i
    n = 1
    while(1):
        if (check_square(x_sq_minus_1 + 1) == True):
            x = sqrt(x_sq_minus_1 + 1)
            # print x
            if x >= x_old:
                x_old = x
                print('x = ', x)
                d = i
            break
        else:
            n = n + 1
            x_sq_minus_1 = i * n * n

print (x,d)
