import numpy as np
import time
from numba import njit
import math
from Tests.Pow import power


@njit
def mr_test(num):
    d, s = num - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2

    rounds = int(math.log2(num))
    for i in range(rounds):
        a = np.random.randint(2, rounds + 2)
        x = power(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for j in range(s - 1):
            x = power(x, 2, num)
            if x == num - 1:
                break
            if x == 1:
                return 0
        else:
            return 0
    return 1


def mr_check(ranges):
    p_c = 2
    time_array = []
    p_c_array = []
    start = time.time()
    for number in ranges:
        for i in ranges.get(number):
            if mr_test(i):
                p_c += 1
        end = time.time()
        time_array.append(end - start)
        p_c_array.append(p_c)
    return time_array, p_c_array
