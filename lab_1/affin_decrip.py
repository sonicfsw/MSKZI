def affine_decrypt(encrip_text, b, a_inv):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.replace('ё', '')
    n = len(alphabet)
    result = ''

    for char in encrip_text.lower():
        if char in alphabet:
            y = alphabet.index(char)
            x = (a_inv * (y - b)) % n
            result += alphabet[x]
        else:
            result += char

    return result

encrip_text = input("Введите зашифрованный текст: ")
b = int(input("Введите ключ 'b': "))
a_inv = int(input("Введите обратное число для 'a': "))
decrypted = affine_decrypt(encrip_text, b, a_inv)
print("Расшифрованный текст:", decrypted)
