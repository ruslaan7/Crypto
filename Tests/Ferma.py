import numpy as np
import time
from numba import njit
import math
from Tests.Pow import power


@njit
def ferma(num):
    rounds = math.ceil(np.log2(num))
    for i in range(rounds):
        a = np.random.randint(2, rounds + 2)
        if power(a, num - 1, num) != 1:
            return 0
    return 1


def f_check(ranges):
    p_c = 2
    time_array = []
    p_c_array = []
    start = time.time()
    for number in ranges:
        for i in ranges.get(number):
            if ferma(i):
                p_c += 1
        end = time.time()
        time_array.append(end - start)
        p_c_array.append(p_c)
    return time_array, p_c_array
