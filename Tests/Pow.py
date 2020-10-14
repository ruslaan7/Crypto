from numba import njit


@njit
def power(a, b, c):
    result, p = 1, a % c
    while b:
        if b & 1:
            result = (result * p) % c
        b >>= 1
        p = (p * p) % c
    return result
