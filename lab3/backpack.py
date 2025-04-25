import random
from sympy import mod_inverse #для упрощения кода, чтобы Эвк

def generate_superincreasing_sequence(n, start=2):
    seq = [random.randint(start, start + 5)]
    for _ in range(n - 1):
        next_val = sum(seq) + random.randint(1, 10)
        seq.append(next_val)
    return seq

def generate_keys(n=8):
    private_key = generate_superincreasing_sequence(n)
    m = sum(private_key) + random.randint(10, 20)
    w = random.randint(2, m - 1)
    while True:
        try:
            w_inv = mod_inverse(w, m)
            break
        except:
            w = random.randint(2, m - 1)

    public_key = [(w * x) % m for x in private_key]
    return private_key, public_key, w, m, w_inv

def int_to_bits(num, length):
    return list(map(int, bin(num)[2:].zfill(length)))

def bits_to_int(bits):
    return int("".join(map(str, bits)), 2)

def encrypt(number, public_key):
    bits = int_to_bits(number, len(public_key))
    print(f"  -> байт {number} в битах: {bits}")
    c = sum(b * pk for b, pk in zip(bits, public_key))
    return c

def decrypt(cipher, private_key, w_inv, m):
    s = (cipher * w_inv) % m
    print(f"  -> расшифровка суммы {cipher}: s = {s}")
    bits = []
    for val in reversed(private_key):
        if val <= s:
            bits.append(1)
            s -= val
        else:
            bits.append(0)
    bits.reverse()
    print(f"     восстановленные биты: {bits}")
    return bits_to_int(bits)

def split_number_to_bytes(number_str):
    number = int(number_str)
    byte_list = []
    while number > 0:
        byte_list.insert(0, number % 256)
        number //= 256
    return byte_list

def combine_bytes_to_number_str(byte_list):
    number = 0
    for b in byte_list:
        number = number * 256 + b
    return str(number)

def backpack_demo():
    number_str = input("Введите число: ")

    private_key, public_key, w, m, w_inv = generate_keys(8)

    print(f"\nПриватный ключ: {private_key}")
    print(f"Открытый ключ:  {public_key}")
    print(f"w = {w}, m = {m}, w^(-1) mod m = {w_inv}\n")

    byte_blocks = split_number_to_bytes(number_str)
    print(f"Число в байтах: {byte_blocks}")

    encrypted_blocks = []
    for b in byte_blocks:
        encrypted_blocks.append(encrypt(b, public_key))
    print(f"\nЗашифрованные блоки: {encrypted_blocks}")

    decrypted_blocks = []
    for c in encrypted_blocks:
        decrypted_blocks.append(decrypt(c, private_key, w_inv, m))
    print(f"\nРасшифрованные байты: {decrypted_blocks}")

    decrypted_str = combine_bytes_to_number_str(decrypted_blocks)
    print(f"\nРасшифрованное число: {decrypted_str}")


if __name__ == "__main__":
    backpack_demo()
