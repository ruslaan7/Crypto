import random
import math
from RSA.generator import generate
from RSA.euclid import euclid
from RSA.crypto import encrypt, decrypt

# Генерируем простые числа p и q
p = generate(128)
q = generate(128)

# Вычисляем модуль n
n = p * q

# Вычисляем функцию Эйлера
eiler = (p - 1) * (q - 1)

# Выбираем случайное и простое e, 2 <= e <= eiler, взаимное простое с eiler
e = random.randint(2, eiler - 1)
while math.gcd(e, eiler) > 1:
    e = random.randint(2, eiler - 1)

# Вычисляется число d
d = euclid(eiler, e) % eiler

# Вводим сообщение
m = input()

# Шифруем сообщение
c = encrypt(m, e, n)

# Расшифровываем сообщение
result = decrypt(c, d, n)

# Выводим расшифрованное сообщение
print(result)
