# -*- coding: utf-8 -*-

# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from common_functions import timing
import numpy as np

def check_leap(year):
    flag = False
    if year % 4 == 0:
        flag = True
        if year % 100 == 0:
            flag = False
            if year % 400 == 0:
                flag = True
    return flag

timer = timing()

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
norm_year = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
leap_year = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])


Jan_1_1900 = days_of_week[0]
day_first = 0

for i in norm_year:
    day_first = day_first + i

Jan_1_1901 = days_of_week[(day_first % 7)]
day_1 = Jan_1_1901

if day_1 == 'Sunday':
    count = 1
else:
    count = 0

for i in range (1901, 2001):
    if check_leap(i):
        for j in leap_year:
            day_1 = days_of_week[((j % 7) + (days_of_week.index(day_1))) % 7]
            if day_1 == 'Sunday':
                count = count + 1
    else:
        for j in norm_year:
            day_1 = days_of_week[((j % 7) + (days_of_week.index(day_1))) % 7]
            if day_1 == 'Sunday':
                count = count + 1

timer("{} Sundays fell on the 1st of the month during the twentieth century".format(count))
