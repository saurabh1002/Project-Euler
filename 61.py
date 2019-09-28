# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

def tri_num(n):
    num = n * (n + 1) * 0.5
    return num

def sqr_num(n):
    num = n * n
    return num
def pent_num(n):
    num = n * ((3 * n) - 1) * 0.5
    return num

def hex_num(n):
    num = n * ((2 * n) - 1)
    return num

def hept_num(n):
    num = n * ((5 * n) - 3) * 0.5
    return num

def oct_num(n):
    num = n * ((3 * n) - 2)
    return num

tri_list = []
tri_last_2 = []
tri_first_2 = []
for i in xrange(45, 140):
    num = tri_num(i)
    tmp = num % 100
    if tmp == tmp % 10:
        continue
    else:
        tri_list.append(num)
        tri_last_2.append(tmp)
        tri_first_2.append((num - tmp) / 100)
# print tri_list
# print tri_first_2
# print tri_last_2

sqr_list = []
sqr_last_2 = []
sqr_first_2 = []
for i in xrange(32, 98):
    num = sqr_num(i)
    tmp = num % 100
    if tmp == tmp % 10:
        continue
    else:
        sqr_list.append(num)
        sqr_last_2.append(tmp)
        sqr_first_2.append((num - tmp) / 100)
# print sqr_list
# print sqr_first_2
# print sqr_last_2

pent_list = []
pent_last_2 = []
pent_first_2 = []
for i in xrange(27, 82):
    num = pent_num(i)
    tmp = num % 100
    if tmp == tmp % 10:
        continue
    else:
        pent_list.append(num)
        pent_last_2.append(tmp)
        pent_first_2.append((num - tmp) / 100)
# print pent_list
# print pent_first_2
# print pent_last_2

hex_list = []
hex_last_2 = []
hex_first_2 = []
for i in xrange(23, 71):
    num = hex_num(i)
    tmp = num % 100
    if tmp == tmp % 10:
        continue
    else:
        hex_list.append(num)
        hex_last_2.append(tmp)
        hex_first_2.append((num - tmp) / 100)
# print hex_list
# print hex_first_2
# print hex_last_2

hept_list = []
hept_last_2 = []
hept_first_2 = []
for i in xrange(21, 64):
    num = hept_num(i)
    tmp = num % 100
    if tmp == tmp % 10:
        continue
    else:
        hept_list.append(num)
        hept_last_2.append(tmp)
        hept_first_2.append((num - tmp) / 100)
# print hept_list
# print hept_first_2
# print hept_last_2

oct_list = []
oct_last_2 = []
oct_first_2 = []
for i in xrange(19, 59):
    num = oct_num(i)
    tmp = num % 100
    if tmp == tmp % 10:
        continue
    else:
        oct_list.append(num)
        oct_last_2.append(tmp)
        oct_first_2.append((num - tmp) / 100)

# print oct_list
# print oct_first_2
# print oct_last_2
