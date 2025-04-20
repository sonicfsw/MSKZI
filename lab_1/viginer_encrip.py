def vigenere_encrypt(text, key, alphabet):
    m = len(alphabet)
    text = text.lower().replace('ё', '')
    key = key.lower().replace('ё', '')

    # расширяем ключ до длины текста
    full_key = (key * (len(text) // len(key) + 1))[:len(text)]

    result = ''
    print("Шаги шифрования:")

    for t_char, k_char in zip(text, full_key):
        if t_char in alphabet and k_char in alphabet:
            x = alphabet.index(t_char)
            k = alphabet.index(k_char)
            y = (x + k) % m
            result += alphabet[y]
            print(f"{t_char}({x}) + {k_char}({k}) = {y} → {alphabet[y]}")
        else:
            result += t_char  # пропускаем символы вне алфавита
            print(f"{t_char} — не из алфавита, оставлен без изменений")

    return result

# Алфавит: 32 буквы (без ё)
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Ввод данных
text = input("Введите фамилию (или любой текст): ")
key = input("Введите имя (ключ): ")

# Шифрование
encrypted = vigenere_encrypt(text, key, alphabet)
print("\n🔐 Зашифрованный текст:", encrypted)
