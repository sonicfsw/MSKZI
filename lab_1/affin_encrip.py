def affine_encrypt(text, a, b):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.replace('ё', '')
    n = len(alphabet)
    result = ''

    for char in text.lower():
        if char in alphabet:
            x = alphabet.index(char)
            y = (a * x + b) % n
            result += alphabet[y]
        else:
            result += char
    return result

text = input("Введите слово для шифрования: ")
a = int(input("Введите ключ 'a' (взаимно простое с 32): "))
b = int(input("Введите ключ 'b': "))


from math import gcd

if gcd(a, 32) != 1:
    print("Ошибка: 'a' должно быть взаимно простым с 32.")
else:
    encrypted = affine_encrypt(text, a, b)
    print("Зашифрованное слово:", encrypted)
