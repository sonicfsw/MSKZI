import random
from sympy import isprime, mod_inverse


# Генерация большого простого числа больше 10^5
def generate_large_prime(start=10 ** 5):
    while True:
        num = random.randint(start, start * 10)
        if isprime(num):
            return num


# Функция для шифрования
def encrypt(m, e, n):
    return pow(m, e, n)
# Функция для расшифровки
def decrypt(c, d, n):
    return pow(c, d, n)

def rsa_demo():
    m = int(input("Введите число для шифрования (целое и меньше модуля): "))
    p = generate_large_prime()
    q = generate_large_prime()
    while p == q:
        q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # часто используемое значение, взято с вики
    while phi % e == 0:
        e = random.randrange(2, phi)

    # Расчёт закрытого ключа d
    d = mod_inverse(e, phi)

    print(f"p = {p}, q = {q}")
    print(f"n = {n}, e = {e}, d = {d}")

    if m >= n:
        print("Число слишком большое для шифрования этим ключом. Повторите с меньшим числом.")
        return
    c = encrypt(m, e, n)
    print(f"Зашифрованное число: {c}")
    m_decrypted = decrypt(c, d, n)
    print(f"Расшифрованное число: {m_decrypted}")


if __name__ == "__main__":
    rsa_demo()
