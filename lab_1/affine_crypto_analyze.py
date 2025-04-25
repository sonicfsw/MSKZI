import math
from collections import Counter

# Русский алфавит без 'ё'
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
m = len(alphabet)  # 32

# Обратный элемент по модулю
def modinv(a, m):
    try:
        return pow(a, -1, m)
    except ValueError:
        return None

# Индекс соответствия
def index_of_coincidence(text):
    n = len(text)
    freqs = Counter(text)
    return sum(f * (f - 1) for f in freqs.values()) / (n * (n - 1)) if n > 1 else 0

# Частота конкретной буквы (0)
def letter_frequency(text, letter):
    total = len(text)
    count = text.count(letter)
    return count / total if total > 0 else 0

# Дешифрование текста
def affine_decrypt(ciphertext, a, b):
    a_inv = modinv(a, m)
    if a_inv is None:
        return None
    decrypted = ''
    for char in ciphertext:
        if char in alphabet:
            y = alphabet.index(char)
            x = (a_inv * (y - b)) % m
            decrypted += alphabet[x]
        else:
            decrypted += char  # сохраняем знаки и пробелы
    return decrypted

def read_ciphertext(path):
    with open(path, encoding='utf-8') as f:
        return f.read().lower()

def brute_force_affine_all(path):
    ciphertext = read_ciphertext(path)
    print(f"🔍 Загружен шифротекст длиной {len(ciphertext)} символов.\n")

    results = []

    for a in range(1, m):
        if math.gcd(a, m) != 1:
            continue  # пропускаем a, не взаимно простые с m
        for b in range(m):
            decrypted = affine_decrypt(ciphertext, a, b)
            if decrypted:
                ic = index_of_coincidence(''.join(c for c in decrypted if c in alphabet))
                freq_o = letter_frequency(decrypted, 'о')
                results.append({
                    'a': a,
                    'b': b,
                    'ic': ic,
                    'freq_o': freq_o,
                    'text': decrypted[:300]  # первые 300 символов
                })

    # Сортировка по близости IC к 0.055
    results.sort(key=lambda x: abs(0.055 - x['ic']))

    print(f"📋 Все {len(results)} вариантов расшифровки:\n")
    for i, res in enumerate(results, 1):
        print(f"{i}. 🔑 a={res['a']}, b={res['b']} | IC={res['ic']:.4f} | 'о'={res['freq_o']:.3f}")
        print(f"   📜 {res['text']}\n")

# Запуск
if __name__ == "__main__":
    brute_force_affine_all("/Users/sonic_fsw/PycharmProjects/MSKZI/lab_1/2 фантастика.txt")
