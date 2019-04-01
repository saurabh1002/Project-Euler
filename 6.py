# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
def timing():
    start_time = time.time()
    return lambda x: print("[{:.9f}s] {}".format(time.time() - start_time, x))

def difference(n):
    sum_of_square = ((n * (n + 1) * ((2 * n) + 1)) / 6)
    square_of_sum = (((n * (n + 1)) * (n * (n + 1))) / 4)
    return square_of_sum - sum_of_square

timer = timing()

ans = difference(100)
timer("{}".format(ans))
