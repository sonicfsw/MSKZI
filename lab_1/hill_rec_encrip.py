import numpy as np

def input_matrix(name):
    matrix = []
    print(f"Введите матрицу {name} (2 строки по 2 числа):")
    for i in range(2):
        row = input(f"  Строка {i+1}: ").strip().split()
        matrix.append(list(map(int, row)))
    return np.array(matrix)

def mod_matrix_mult(a, b, m):
    return np.dot(a, b) % m

def recurrent_hill_encrypt(text, K0, K1, alphabet):
    m = len(alphabet)
    text = text.lower().replace('ё', '')

    # дополняем, если нечетное количество букв
    if len(text) % 2 != 0:
        text += 'ю'

    blocks = [text[i:i+2] for i in range(0, len(text), 2)]
    matrices = [K0, K1]

    result = ''
    print("\nШаги шифрования:")

    for i, block in enumerate(blocks):
        if i >= 2:
            new_K = mod_matrix_mult(matrices[i-2], matrices[i-1], m)
            matrices.append(new_K)

        current_matrix = matrices[i]
        vector = np.array([alphabet.index(c) for c in block]).reshape(2, 1)
        encrypted_vector = current_matrix @ vector % m
        encrypted_block = ''.join(alphabet[int(v)] for v in encrypted_vector.flatten())

        print(f"{block} → {[alphabet.index(c) for c in block]} → {encrypted_block}")
        result += encrypted_block

    return result

# --- Алфавит: 31 буква (без ё и я) ---
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэю'

# --- Ввод двух стартовых матриц 2×2 ---
K0 = input_matrix("K0")
K1 = input_matrix("K1")

# --- Ввод текста ---
text = input("\nВведите слово для шифрования: ")

# --- Шифрование ---
encrypted = recurrent_hill_encrypt(text, K0, K1, alphabet)
print("\n🔐 Зашифрованный текст:", encrypted)
