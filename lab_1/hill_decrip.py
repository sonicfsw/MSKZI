import numpy as np

def modinv(a, m):
    """Обратное число по модулю m"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Обратного элемента для {a} по модулю {m} не существует")

def matrix_mod_inv_3x3(matrix, modulus):
    """Ручное нахождение обратной матрицы по модулю"""
    det = int(round(np.linalg.det(matrix))) % modulus
    if np.gcd(det, modulus) != 1:
        raise ValueError(f"Определитель {det} не взаимно прост с {modulus}")
    det_inv = modinv(det, modulus)

    cofactors = np.zeros((3,3), dtype=int)
    for row in range(3):
        for col in range(3):
            minor = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
            sign = (-1) ** (row + col)
            cofactors[row, col] = sign * int(round(np.linalg.det(minor)))

    adjugate = cofactors.T
    inv_matrix = (det_inv * adjugate) % modulus
    return inv_matrix

def hill3_decrypt(blocks, key_matrix, alphabet):
    m = len(alphabet)
    inv_matrix = matrix_mod_inv_3x3(key_matrix, m)

    result = ''
    print("\nШаги дешифровки:")
    for block in blocks:
        if len(block) != 3:
            print(f"Блок '{block}' некорректен (не 3 символа), пропускаем.")
            continue

        indices = [alphabet.index(c) for c in block]
        vector = np.array(indices).reshape(3, 1)
        decrypted_vector = inv_matrix @ vector % m
        decrypted_block = ''.join(alphabet[int(i)] for i in decrypted_vector.flatten())
        print(f"{block} → {indices} → {decrypted_vector.flatten().tolist()} → {decrypted_block}")
        result += decrypted_block

    return result

# --- Алфавит из 31 буквы (без ё и я) ---
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэю'

# --- Ввод матрицы ---
print("Введите ключевую матрицу 3x3 (по строкам, через пробел):")
key_matrix = []
for i in range(3):
    row = input(f"Строка {i+1}: ")
    key_matrix.append(list(map(int, row.strip().split())))
key_matrix = np.array(key_matrix)

# --- Ввод зашифрованных блоков ---
print("\nВведите зашифрованные блоки по 3 буквы (Enter без ввода — завершить):")
blocks = []
while True:
    block = input("Блок: ").strip().lower()
    if not block:
        break
    blocks.append(block)

# --- Дешифровка ---
try:
    decrypted = hill3_decrypt(blocks, key_matrix, alphabet)
    print("\n🔓 Расшифрованное слово:", decrypted)
except Exception as e:
    print("Ошибка при дешифровке:", e)
