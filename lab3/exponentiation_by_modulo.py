def mod_pow(a, b, m):
    result = 1
    a = a % m

    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b = b // 2

    return result

a = int(input("число, которое нужно возвести 'a': "))
b = int(input("значение степени 'b': "))
m = int(input("модуль 'm': "))
result = mod_pow(a, b, m)
print("Результат возведения в степени:", result)