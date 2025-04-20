# аффинная расшифровка: D(x) = a_inv * (x - b) mod m

def mod_inverse(a, m):
    """Находит обратный элемент a по модулю m"""
    for i in range(m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f"Обратный элемент для a={a} по модулю {m} не найден")

def affine_decrypt(ciphertext, a, b, alphabet):
    m = len(alphabet)
    a_inv = mod_inverse(a, m)
    decrypted = ""

    for char in ciphertext:
        if char in alphabet:
            x = alphabet.index(char)
            decrypted += alphabet[(a_inv * (x - b)) % m]
        else:
            decrypted += char  # если символ вне алфавита, оставляем как есть
    return decrypted

# ==== НАСТРОЙКИ ====
a = 3       # значение a
b = 30        # значение b
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"  # кириллица (можно поменять)

# ==== ЧТЕНИЕ И РАСШИФРОВКА ====
with open("1.rtf", "r", encoding="utf-8") as file:
    encrypted_text = file.read()

decrypted_text = affine_decrypt(encrypted_text.lower(), a, b, alphabet)

print("Расшифрованный текст:\n", decrypted_text)

# ==== (по желанию) СОХРАНЕНИЕ В ФАЙЛ ====
with open("2.rtf", "w", encoding="utf-8") as file:
    file.write(decrypted_text)
