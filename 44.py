from math import *

def check_triangle(num):
    num = 1 + sqrt(1 + (24 * num))
    if (num % 6 == 0):
        return True
    else:
        return False

for a in range (1, 10000):
    for b in range(2, 10000):
        if b > a:
            j = (3 * a * a - a) * 0.5
            k = (3 * b * b - b) * 0.5
            if check_triangle(j + k):
                if check_triangle(k - j):
                    print k - j
