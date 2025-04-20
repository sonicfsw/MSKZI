import collections

# Функция для частотного анализа
def frequency_analysis(text):
    freq = collections.Counter(text)
    total_chars = sum(freq.values())
    probabilities = {char: count / total_chars for char, count in freq.items()}
    return freq, probabilities

# Подсчет символов без пробелов
def count_chars_without_spaces(text):
    return len(text.replace(" ", ""))

# Чтение текста
with open("1.rtf", "r", encoding="utf-8") as f:
    text = f.read()

# Частотный анализ
frequencies, probabilities = frequency_analysis(text)

# Сортировка по убыванию частоты
sorted_freq = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

# Вывод результатов в консоль
print("Частоты символов (по убыванию):")
for char, count in sorted_freq:
    print(f"'{char}': {count}")

print("\nВероятности появления символов (по убыванию):")
for char, _ in sorted_freq:
    print(f"'{char}': {probabilities[char]:.4f}")

# Подсчет количества символов без пробелов
char_count = count_chars_without_spaces(text)
print(f"\nКоличество символов без пробелов: {char_count}")
