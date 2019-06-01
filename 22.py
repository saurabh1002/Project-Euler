f = open("names.txt", "r").read()

a = ''
list = []
for x in f:
    if (x != ','):
        if x != '"':
            a = a + x
    if x == ',':
        # print a
        list.append(a)
        a = ''

dict = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8", "I": "9", "J": "10", "K": "11", "L": "12",
        "M": "13", "N": "14", "O": "15", "P": "16", "Q": "17", "R": "18", "S": "19", "T": "20", "U": "21", "V": "22", "W": "23", "X": "24",
        "Y": "25", "Z": "26"}
        
dict_new = {}

for j in xrange(0, 20):
    for i in list:
        try:
            temp = dict.get(i[j])
            dict_new[i] = int(temp)
        except IndexError:
            dict_new[i] = 0

dict_new = sorted(dict_new.items(), key = lambda kv:(kv[1], kv[0]))
print dict_new

total = 0
k = 1
for i in dict_new:
    sum = 0.0
    print i[0]
    for j in xrange(0, len(i[0])):
        n = int(dict.get(i[0][j]))
        sum = sum + n
    print sum, k
    total = total + (sum * k)
    k = k + 1

print total
