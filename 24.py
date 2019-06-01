# -*- coding: utf-8 -*-

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import copy

list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lexi_perm = []
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
                                    list_i = copy.copy(list_h)
                                    list_i.remove(i)
                                    # print i
                                    for j in list_i:
                                        # print j
                                        lexi_perm.append(a + b + c + d + e + f + g + h + i + j)
                                        print(lexi_perm[-1])

print lexi_perm[999999]
