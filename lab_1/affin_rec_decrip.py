def modinv(a, n):
    """Находит обратное по модулю число"""
    a = a % n
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    raise Exception(f"Обратного элемента для {a} по модулю {n} не существует")

def affine_decrypt(cipher_text, a0, a1, b0, b1):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.replace('ё', '')
    n = len(alphabet)
    cipher_text = cipher_text.lower()

    a_seq = [a0, a1]
    b_seq = [b0, b1]

    for i in range(2, len(cipher_text)):
        a_seq.append(a_seq[i-2] * a_seq[i-1])
        b_seq.append(b_seq[i-2] + b_seq[i-1])

    result = ''
    print("Шаги дешифровки:")

    for i, char in enumerate(cipher_text):
        if char in alphabet:
            y = alphabet.index(char)
            a = a_seq[i]
            b = b_seq[i]
            try:
                a_inv = modinv(a, n)
                x = (a_inv * (y - b)) % n
                result_char = alphabet[x]
                result += result_char
                print(f"{char} ({y}) → a={a}, b={b}, a⁻¹={a_inv} → ({a_inv} * ({y} - {b})) % {n} = {x} → {result_char}")
            except Exception as e:
                print(f"Ошибка для символа '{char}': {e}")
                result += '?'
        else:
            result += char
            print(f"{char} — не из алфавита, оставлен без изменений")

    return result

# --- Ввод ---
cipher_text = input("Введите зашифрованный текст: ")
a0 = int(input("Введите a₀: "))
a1 = int(input("Введите a₁: "))
b0 = int(input("Введите b₀: "))
b1 = int(input("Введите b₁: "))

decrypted = affine_decrypt(cipher_text, a0, a1, b0, b1)
print("\nРасшифрованный текст:", decrypted)
