import numpy as np

mod = 37
X = np.array([[16, 9],
              [17, 2]])
Y = np.array([[36, 25],
              [12, 28]])
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Обратного элемента для {a} по модулю {m} не существует")

def matrix_modinv_2x2(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix))) % modulus
    det_inv = modinv(det, modulus)

    inv_matrix = np.array([
        [ matrix[1,1], -matrix[0,1]],
        [-matrix[1,0],  matrix[0,0]]
    ]) * det_inv

    inv_matrix = inv_matrix % modulus
    return inv_matrix

X_inv = matrix_modinv_2x2(X, mod)
K = np.dot(Y, X_inv) % mod

print("Найденная матрица ключа K:")
print(K)
