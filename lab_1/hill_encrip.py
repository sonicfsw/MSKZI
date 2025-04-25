import numpy as np
def hill_encrypt(text, key_matrix, alphabet):
    n = len(alphabet)
    text = text.lower().replace('ё', '')
    text = text.lower().replace('я', '')
    while len(text) % 3 != 0:
        text += 'а'
    result = ''
    print("Шаги шифрования:")

    for i in range(0, len(text), 3):
        block = text[i:i + 3]
        vector = np.array([[alphabet.index(block[0])],
                           [alphabet.index(block[1])],
                           [alphabet.index(block[2])]])
        enc_vector = key_matrix @ vector % n
        encrypted_block = ''.join(alphabet[int(i % n)] for i in enc_vector.flatten())
        result += encrypted_block
        print(f"{block} → {[alphabet.index(c) for c in block]} → {encrypted_block}")
    return result

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэю'.replace('ё', '').replace('я', '')
key_matrix = np.array([
    [1, 8, 0],
    [2, 2, 0],
    [0, 4, 1]
])

text = input("Введите фамилию для шифрования: ")
encrypted = hill_encrypt(text, key_matrix, alphabet)
print("\nЗашифрованная фамилия:", encrypted)

