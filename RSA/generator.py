from RSA.MR import miller_rabin
import random


def generate(bits):
    number = random.getrandbits(bits)
    while miller_rabin(number) == 0:
        number = random.getrandbits(bits)

    return number
