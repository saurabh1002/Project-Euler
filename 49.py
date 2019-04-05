from math import *

def check_prime(number):
    if (number == 1):
        return 0
    if (number == 2 or number == 3):
        return 1
    prime_flag = 1
    i = 2
    while (i <= sqrt(number)):
        if(number % i == 0):
            prime_flag = 0
            break
        i = i + 1
    if (prime_flag == 1):
        return 1

list = []
list_diff = []
for i in range (1001, 10000, 2):
    if (check_prime(i) == 1):
        list.append(i)
print list

for i in range (0, len(list) - 1):
    list_diff.append(list[i + 1] - list[i])

print list_diff
