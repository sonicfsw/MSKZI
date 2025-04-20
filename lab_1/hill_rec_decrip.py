import numpy as np

# Алфавит: 31 буква (без ё и я)
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэю'


def modinv(a, m):
    """Обратное число по модулю"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Обратного элемента для {a} по модулю {m} не существует")


def inverse_matrix_2x2(matrix, modulus):
    """Обратная матрица 2x2 по модулю"""
    a, b = matrix[0]
    c, d = matrix[1]
    det = (a * d - b * c) % modulus
    det_inv = modinv(det, modulus)

    # Обратная матрица
    inv = np.array([[d, -b],
                    [-c, a]]) * det_inv
    return inv % modulus


def input_matrix(name):
    matrix = []
    print(f"Введите матрицу {name} (2 строки по 2 числа):")
    for i in range(2):
        row = input(f"  Строка {i + 1}: ").strip().split()
        matrix.append(list(map(int, row)))
    return np.array(matrix)


def hill_recurrent_decrypt(blocks, K0, K1, alphabet):
    m = len(alphabet)
    matrices = [K0, K1]
    result = ''

    print("\nШаги дешифровки:")

    for i, block in enumerate(blocks):
        if len(block) != 2:
            print(f"Блок '{block}' некорректен, пропущен.")
            continue

        if i >= 2:
            new_K = np.dot(matrices[i - 2], matrices[i - 1]) % m
            matrices.append(new_K)

        current_matrix = matrices[i]
        inverse = inverse_matrix_2x2(current_matrix, m)

        y_vector = np.array([alphabet.index(c) for c in block]).reshape(2, 1)
        x_vector = np.dot(inverse, y_vector) % m
        decrypted_block = ''.join(alphabet[int(x)] for x in x_vector.flatten())

        print(f"{block} → {y_vector.flatten().tolist()} → {decrypted_block}")
        result += decrypted_block

    return result


# --- Ввод матриц ---
K0 = input_matrix("K0")
K1 = input_matrix("K1")

# --- Ввод блоков ---
print("\nВведите зашифрованные блоки по 2 буквы (Enter без ввода — завершить):")
blocks = []
while True:
    block = input("Блок: ").strip().lower()
    if not block:
        break
    blocks.append(block)

# --- Дешифровка ---
try:
    decrypted = hill_recurrent_decrypt(blocks, K0, K1, alphabet)
    print("\n🔓 Расшифрованный текст:", decrypted)
except Exception as e:
    print("❌ Ошибка:", e)
