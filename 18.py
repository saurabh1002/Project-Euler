# Find the maximum total from top to bottom of the triangle below:

from common_functions import timing
import numpy as np 

timer = timing()

p0 = np.array([75])
p1 = np.array([95, 64])
p2 = np.array([17, 47, 82])
p3 = np.array([18, 35, 87, 10])
p4 = np.array([20, 4, 82, 47, 65])
p5 = np.array([19, 1, 23, 75, 3, 34])
p6 = np.array([88, 2, 77, 73, 7, 63, 67])
p7 = np.array([99, 65, 4, 28, 6, 16, 70, 92])
p8 = np.array([41, 41, 26, 56, 83, 40, 80, 70, 33])
p9 = np.array([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
p10 = np.array([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
p11 = np.array([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
p12 = np.array([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
p13 = np.array([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
p14 = np.array([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])
p = np.array([p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14])

for i in range (len(p) - 1, 0, -1):
    for j in range (0, len(p[i - 1])):
        p[i - 1][j] = max((p[i - 1][j] + p[i][j]), p[i - 1][j] + p[i][j + 1])

timer("The maximum total is {}".format(p[0]))
