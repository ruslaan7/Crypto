import numpy as np
import time
from numba import njit
import math
from Tests.Pow import power


@njit
def sh(num):
    rounds = math.ceil(np.log2(num))
    for i in range(rounds):
        a = np.random.randint(2, num)
        f = power(a, (num - 1) // 2, num)
        s = legandra(a, num)
        if np.gcd(a, num) > 1 or f != s % num:
            return 0
    return 1


def sh_check(ranges):
    p_c = 2
    time_array = []
    p_c_array = []
    start = time.time()
    for number in ranges:
        for i in ranges.get(number):
            if sh(i):
                p_c += 1
        end = time.time()
        time_array.append(end - start)
        p_c_array.append(p_c)
    return time_array, p_c_array


@njit
def legandra(a, p):
    if a == 0 or a == 1:
        return a
    if a % 2 == 0:
        r = legandra(a // 2, p)
        if p * p - 1 & 8 != 0:
            r *= -1
    else:
        r = legandra(p % a, a)
        if (a - 1) * (p - 1) & 4 != 0:
            r *= -1
    return r
