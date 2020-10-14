import numpy as np
import time
from numba import njit
import math
from Tests.Pow import power


@njit
def leman(num):
    rounds = math.ceil(np.log2(num))
    for i in range(rounds):
        a = np.random.randint(2, num - 1)
        f = power(a, (num - 1)//2, num)
        if f != 1 % num and f != -1 % num:
            return 0
    return 1


def l_check(ranges):
    p_c = 2
    time_array = []
    p_c_array = []
    start = time.time()
    for number in ranges:
        for i in ranges.get(number):
            if leman(i):
                p_c += 1
        end = time.time()
        time_array.append(end - start)
        p_c_array.append(p_c)
    return time_array, p_c_array
