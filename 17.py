# -*- coding: utf-8 -*-

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

from common_functions import timing

timer = timing()

units = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
tens = ("ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
exception = ("eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")

sum_unit = 0
sum_ten = 0
sum_exception = 0
len_hundred = len("hundred")
len_and = len("and")
len_thousand = len("thousand")

for i in units:
    sum_unit = sum_unit + len(i)

for i in tens:
    sum_ten = sum_ten + len(i)

for i in exception:
    sum_exception = sum_exception + len(i)

sum_unit_total = sum_unit * 90
sum_hundred_total = sum_unit * 100
sum_hundred = len_hundred * 900
sum_and = len_and * 99 * 9
sum_exception = sum_exception * 10
sum_ten = (sum_ten * 10) + ((sum_ten - 3) * 90)

total = sum_and + sum_ten + sum_unit_total + sum_hundred_total + sum_exception + sum_hundred + len_thousand + 3

timer("{} letters will be used".format(total))
