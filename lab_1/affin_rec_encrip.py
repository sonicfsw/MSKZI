def afinno_encrypt(text, a0, a1, b0, b1):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.replace('ё', '')
    n = len(alphabet)
    text = text.lower()
    a_seq = [a0, a1]
    b_seq = [b0, b1]
    #новые значения a и b
    for i in range(2, len(text)):
        a_seq.append(a_seq[i - 2] * a_seq[i - 1])
        b_seq.append(b_seq[i - 2] + b_seq[i - 1])

    encrypted = ''
    print("Шаги шифрования:")
    for i, char in enumerate(text):
        if char in alphabet:
            x = alphabet.index(char)
            a = a_seq[i]
            b = b_seq[i]
            y = (a * x + b) % n
            encrypted_char = alphabet[y]
            encrypted += encrypted_char
            print(f"{char} ({x}) → a={a}, b={b} → ({a}*{x}+{b}) % {n} = {y} → {encrypted_char}")
        else:
            encrypted += char
            print(f"{char} — не из алфавита, оставлен без изменений")

    return encrypted

text = input("Введите слово для шифрования: ")
a0 = int(input("Введите a0: "))
a1 = int(input("Введите a1: "))
b0 = int(input("Введите b0: "))
b1 = int(input("Введите b1: "))
result = afinno_encrypt(text, a0, a1, b0, b1)
print("\nЗашифрованное слово:", result)

