def modinv(a, n):
    #нахождение обратного по модулю числа (a⁻¹ mod n), чтото типо брутфорса
    a = a % n
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    raise ValueError(f"Обратного элемента для {a} по модулю {n} не существует")

def affine_decrypt(encrip_text, a, b):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.replace('ё', '')
    n = len(alphabet)
    result = ''

    try:
        a_inv = modinv(a, n)
    except ValueError as e:
        print("Ошибка:", e)
        return ''

    for char in encrip_text.lower():
        if char in alphabet:
            y = alphabet.index(char)
            x = (a_inv * (y - b)) % n
            result += alphabet[x]
        else:
            result += char
    return result

encrip_text = input("Введите зашифрованный текст: ")
a = int(input("Введите ключ 'a': "))
b = int(input("Введите ключ 'b': "))
decrypted = affine_decrypt(encrip_text, a, b)
print("Расшифрованный текст:", decrypted)