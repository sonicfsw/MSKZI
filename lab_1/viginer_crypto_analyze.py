import sys
import re
from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
m = len(alphabet)

# Индекс соответствия
def index_of_coincidence(text):
    N = len(text)
    freqs = Counter(text)
    return sum(f * (f - 1) for f in freqs.values()) / (N * (N - 1)) if N > 1 else 0

# Подбор лучшего сдвига по частоте "о"
def guess_key_letter(group):
    max_score = 0
    best_shift = 0
    for shift in range(m):
        decrypted = ''.join(
            alphabet[(alphabet.index(c) - shift) % m] for c in group
        )
        freq_o = decrypted.count('о') / len(decrypted)
        if freq_o > max_score:
            max_score = freq_o
            best_shift = shift
    return best_shift

def vigenere_decrypt(ciphertext, key):
    decrypted = ''
    key_indices = [alphabet.index(k) for k in key]
    for i, char in enumerate(ciphertext):
        if char in alphabet:
            shift = key_indices[i % len(key)]
            x = (alphabet.index(char) - shift) % m
            decrypted += alphabet[x]
        else:
            decrypted += char
    return decrypted

# Криптоанализ
def vigenere_cryptanalysis(text, max_key_len=15):
    text = ''.join(c for c in text.lower() if c in alphabet)

    print(f"🔍 Длина текста: {len(text)} символов\n")

    probable_keys = []

    for key_len in range(1, max_key_len + 1):
        groups = ['' for _ in range(key_len)]
        for i, char in enumerate(text):
            groups[i % key_len] += char
        avg_ic = sum(index_of_coincidence(g) for g in groups) / key_len
        print(f"🔑 Возможная длина ключа {key_len}: IC = {avg_ic:.4f}")
        if 0.04 < avg_ic < 0.07:
            probable_keys.append((key_len, avg_ic))

    if not probable_keys:
        print("❌ Не удалось определить длину ключа.")
        return

    best_key_len = sorted(probable_keys, key=lambda x: abs(0.055 - x[1]))[0][0]
    print(f"\n✅ Предполагаемая длина ключа: {best_key_len}")

    key = ''
    for i in range(best_key_len):
        group = text[i::best_key_len]
        shift = guess_key_letter(group)
        key += alphabet[shift]

    print(f"🔐 Предположительный ключ: {key}\n")

    plaintext = vigenere_decrypt(text, key)
    print("📜 Фрагмент расшифровки:\n")
    print(plaintext[:500])

def read_file(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    filepath = "/Users/sonic_fsw/PycharmProjects/MSKZI/lab_1/etext2.txt"
    text = read_file(filepath)
    vigenere_cryptanalysis(text)
