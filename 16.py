# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

from math import *
num = 2 ** 1000
print num
sum = 0
while num !=0:
    sum = sum + (num % 10)
    num = (num - (num % 10))/10
    print (num, sum)

print sum
