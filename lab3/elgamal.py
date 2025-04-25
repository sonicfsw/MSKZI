import random
from sympy import isprime, primitive_root, mod_inverse

def generate_large_prime(start=10**50):
    while True:
        p = random.randint(start, start * 10)
        if isprime(p):
            return p

# Шифрование по Эль-Гамалю
def elgamal_encrypt(m, p, g, y):
    k = random.randint(1, p - 1)
    a = pow(g, k, p)
    b = (m * pow(y, k, p)) % p
    return a, b

# Расшифровка по Эль-Гамалю
def elgamal_decrypt(a, b, p, x):
    s = pow(a, x, p)
    s_inv = mod_inverse(s, p)
    m = (b * s_inv) % p
    return m

# Основная логика
def elgamal_demo():
    m = int(input("Введите число для шифрования (целое и меньше простого p): "))
    p = generate_large_prime()
    g = primitive_root(p)
    x = random.randint(1, p - 1)
    y = pow(g, x, p)

    print(f"p = {p}, g = {g}")
    print(f"Секретный ключ x = {x}")
    print(f"Открытый ключ y = {y}")

    if m >= p:
        print("Ошибка: число должно быть меньше p.")
        return


    a, b = elgamal_encrypt(m, p, g, y)
    print(f"Зашифровано как: a = {a}, b = {b}")
    decrypted = elgamal_decrypt(a, b, p, x)
    print(f"Расшифрованное число: {decrypted}")

if __name__ == "__main__":
    elgamal_demo()
