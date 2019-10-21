# -*- coding: utf-8 -*-

# Using names.txt(right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

from common_functions import timing

timer = timing()

f = open("names.txt", "r").read()

a = ''
list = []
for x in f:
    if (x != ','):
        if x != '"':
            a = a + x
    if x == ',':
        list.append(a)
        a = ''

dict = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9", "J": "10", "K": "11", "L": "12",
        "M": "13", "N": "14", "O": "15", "P": "16", "Q": "17", "R": "18", "S": "19", "T": "20", "U": "21", "V": "22", "W": "23", "X": "24",
        "Y": "25", "Z": "26"}
        
dict_new = {}

for j in range(0, 20):
    for i in list:
        try:
            temp = dict.get(i[j])
            dict_new[i] = int(temp)
        except IndexError:
            dict_new[i] = 0

dict_new = sorted(dict_new.items(), key = lambda kv:(kv[1], kv[0]))

total = 0
k = 1
for i in dict_new:
    sum = 0.0
    for j in range(0, len(i[0])):
        n = int(dict.get(i[0][j]))
        sum = sum + n
    total = total + (sum * k)
    k = k + 1

timer("The total of all the name scores in the file is {}".format(total))
