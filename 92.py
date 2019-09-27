# -*- coding: utf-8 -*-

# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?


def toString(List):
    return ''.join(List)


def permute(a, l, r, lst):
    print('in perm')
    if l == r:
        num = int(toString(a))
        if num in num_lst:
            lst.append(num)
            num_lst.remove(num)
    else:
        for i in xrange(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r, lst)
            a[l], a[i] = a[i], a[l]

def square_sum(num):
    sum = 0
    while (num != 0):
        l = num % 10
        sum = sum + (l * l)
        num = (num - l) /10
    return sum

list_1 = [1]
list_89 = [89]
sum_89 = 0
num_lst = []

for i in xrange(9999999, 1, -1):
    num_lst.append(i)

while len(num_lst) != 0:
    input('1')
    lst = []  
    i = num_lst[0]
    a = list(str(i))
    n = len(str(i))
    permute(a, 0, n-1, lst)
    temp = [] + lst
    print temp
    input('2')
    next = square_sum(i)
    while (next not in list_1 and next not in list_89 and next not in temp):
        input('3')
        print (next)
        temp.append(next)
        num_lst.remove(next)
        next = square_sum(next)
    if next in list_1:
        print ('1', temp)
        list_1 = list_1 + temp
    else:
        print ('89', temp)
        list_89 = list_89 + temp
        sum_89 = sum_89 + len(temp)
    

print sum_89

