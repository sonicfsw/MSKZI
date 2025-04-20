def vigenere_decrypt(cipher_text, key, alphabet):
    m = len(alphabet)
    cipher_text = cipher_text.lower().replace('ё', '')
    key = key.lower().replace('ё', '')

    full_key = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]

    result = ''
    print("Шаги дешифровки:")

    for c_char, k_char in zip(cipher_text, full_key):
        if c_char in alphabet and k_char in alphabet:
            y = alphabet.index(c_char)
            k = alphabet.index(k_char)
            x = (y - k + m) % m
            result += alphabet[x]
            print(f"{c_char}({y}) - {k_char}({k}) = {x} → {alphabet[x]}")
        else:
            result += c_char
            print(f"{c_char} — не из алфавита, оставлен без изменений")

    return result

# Алфавит: 32 буквы (без ё)
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Ввод данных
cipher_text = input("Введите зашифрованный текст: ")
key = input("Введите имя (ключ): ")

# Дешифрование
decrypted = vigenere_decrypt(cipher_text, key, alphabet)
print("\n🔓 Расшифрованный текст:", decrypted)
