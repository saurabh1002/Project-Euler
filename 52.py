# -*- coding: utf-8 -*-
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def get_sorted_digits(number):
    list = []
    while number != 0:
        list.append(str(number % 10))
        number = (number - (number % 10)) / 10
    list.sort(key=int)
    return list

i = 100000
while 1:
    i = i + 1
    if get_sorted_digits(i) == get_sorted_digits(i * 5):
        if get_sorted_digits(i) == get_sorted_digits(i * 3):
            if get_sorted_digits(i) == get_sorted_digits(i * 6):
                if get_sorted_digits(i) == get_sorted_digits(i * 4):
                    if get_sorted_digits(i) == get_sorted_digits(i * 2):
                        print i 
                        break
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue
