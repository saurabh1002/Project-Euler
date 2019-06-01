# -*- coding: utf-8 -*-

#   Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
#                                           21 22 23 24 25
#                                           20  7  8  9 10
#                                           19  6  1  2 11
#                                           18  5  4  3 12
#                                           17 16 15 14 13
#
#   It can be verified that the sum of the numbers on the diagonals is 101.
#   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

size_of_spiral = 1001

diag_ur = 0
for i in xrange (1, size_of_spiral + 1, 2):
    diag_ur = diag_ur + (i ** 2)

diag_ll = 0
for i in xrange (2, size_of_spiral, 2):
    diag_ll = diag_ll + (i ** 2) + 1

diag_ul = diag_ll + (((size_of_spiral - 1) / 2) * (((size_of_spiral - 1) / 2) + 1))
diag_lr = diag_ur - 1 - (3 * (((size_of_spiral - 1) / 2) * (((size_of_spiral - 1) / 2) + 1)))

sum = diag_ul + diag_ur + diag_lr + diag_ll
print sum
