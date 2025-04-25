from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabet_size = len(alphabet)
most_common_letter = 'о'

def find_probable_key_letter(cipher_letter):
    y = alphabet.index(cipher_letter)
    o_index = alphabet.index(most_common_letter)
    key_index = (y - o_index + alphabet_size) % alphabet_size
    return alphabet[key_index]

def vigenere_crack(cipher_text, max_key_length=10):
    cipher_text = cipher_text.lower().replace('ё', '')
    cipher_text = ''.join([c for c in cipher_text if c in alphabet])

    for key_len in range(1, max_key_length + 1):
        print(f"\n Пробуем длину ключа: {key_len}")
        key = ''

        for i in range(key_len):
            nth_letters = cipher_text[i::key_len]
            freq = Counter(nth_letters)
            most_common = freq.most_common(1)[0][0]
            key_letter = find_probable_key_letter(most_common)
            key += key_letter
            print(f"Позиция {i+1}: чаще всего '{most_common}' → предполагаем букву ключа: '{key_letter}'")

        print(" Предполагаемый ключ:", key)
        decrypted = vigenere_decrypt(cipher_text, key, alphabet)
        print(" Возможная расшифровка:", decrypted[:100], "...\n")

def vigenere_decrypt(cipher_text, key, alphabet):
    m = len(alphabet)
    full_key = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]

    result = ''
    for c_char, k_char in zip(cipher_text, full_key):
        if c_char in alphabet and k_char in alphabet:
            y = alphabet.index(c_char)
            k = alphabet.index(k_char)
            x = (y - k + m) % m
            result += alphabet[x]
        else:
            result += c_char
    return result

cipher_text = input("Введите зашифрованный текст: ")
vigenere_crack(cipher_text)
