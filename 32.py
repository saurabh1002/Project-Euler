# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import copy

list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pan = []
sum = 0
for a in list:
    list_a = copy.copy(list)
    list_a.remove(a)
    # print a
    for b in list_a:
        list_b = copy.copy(list_a)
        list_b.remove(b)
        # print b
        for c in list_b:
            list_c = copy.copy(list_b)
            list_c.remove(c)
            # print c
            for d in list_c:
                list_d = copy.copy(list_c)
                list_d.remove(d)
                # print d
                for e in list_d:
                    list_e = copy.copy(list_d)
                    list_e.remove(e)
                    # print e
                    for f in list_e:
                        list_f = copy.copy(list_e)
                        list_f.remove(f)
                        # print f
                        for g in list_f:
                            list_g = copy.copy(list_f)
                            list_g.remove(g)
                            # print g
                            for h in list_g:
                                list_h = copy.copy(list_g)
                                list_h.remove(h)
                                # print h
                                for i in list_h:
                                    if ((int(a + b) * int(c + d + e)) == (int(f + g + h + i))):
                                        if (int(f + g + h + i) in pan):
                                            pass
                                        else:
                                            pan.append(int(f + g + h + i))
                                            sum = sum + int(f + g + h + i)
                                    elif ((int(a + b + c) * int(d + e)) == (int(f + g + h + i))):
                                        if (int(f + g + h + i) in pan):
                                            pass
                                        else:
                                            pan.append(int(f + g + h + i))
                                            sum = sum + int(f + g + h + i)
                                    elif ((int(a) * int(b + c + d + e)) == (int(f + g + h + i))):
                                        if (int(f + g + h + i) in pan):
                                            pass
                                        else:
                                            pan.append(int(f + g + h + i))
                                            sum = sum + int(f + g + h + i)
                                    elif ((int(a + b + c + d) * int(e)) == (int(f + g + h + i))):
                                        if (int(f + g + h + i) in pan):
                                            pass
                                        else:
                                            pan.append(int(f + g + h + i))
                                            sum = sum + int(f + g + h + i)
print sum
