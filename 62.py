# -*- coding: utf-8 -*-

# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

import copy
from math import *


def toString(List):
    return ''.join(List)

def permute(a, l, r, lst):
    if l == r:
        num = int(toString(a))
        if (num not in lst) and (num not in reject):
            cond_1 = (num % 10 == 0) and (num % 1000 != 0)
            cond_2 = (num % 10 == 5) and (num % 25 != 0)
            cond_3 = (num % 2 == 0) and (num % 4 != 0)
            
            if (cond_1) or (cond_2) or (cond_3):
                reject.append(num)
                pass
            else:
                x = (num ** (1./3))
                y = round((num ** (1./3)))
                cond_7 = abs(x - y) <= 0.0000001
                if cond_7:
                    num_lst.append(round(num ** (1./3)))
                    lst.append(num)
                else:
                    reject.append(num)
    else:
        for i in xrange(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, lst)
            a[l], a[i] = a[i], a[l]

j = 345
num_lst = []
reject =[]
while (1):
    count = 0
    c = j ** 3
    a = list(str(c))
    n = len(str(c))
    lst = []
    permute(a, 0, n-1, lst)
    print lst
    if len(lst) == 5:
        print (j)
        break
    else:
        while(1):
            j = j + 1
            if j in num_lst:
                print ('in')
                continue
            else:
                break
