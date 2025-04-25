def fermat_test(p, a):
    if p <= 3:
        return "Введите число больше 3"

    if a <= 1 or a >= p:
        return f"Основание a должно быть в диапазоне от 2 до {p - 1}"

    result = pow(a, p - 1, p)
    if result == 1:
        return f"{p} — возможно простое (при a = {a})"
    else:
        return f"{p} — составное (при a = {a})"

try:
    p = int(input("Введите число p для проверки (p > 3): "))
    a = int(input(f"Введите основание a (2 ≤ a < {p}): "))
    print(fermat_test(p, a))
except ValueError:
    print("Ошибка: введите целые числа.")
