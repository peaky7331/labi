#Восьмеричные числа не превышающие 2048**10. Список используемых цифр выводится отдельно прописью.

digit_to_word = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'четыре',
    '5': 'пять',
    '6': 'шесть',
    '7': 'семь',
}

def number_to_words(number):
    return [digit_to_word[digit] for digit in number]

max_value_decimal = 2048 ** 10

with open('numbers.txt', 'r') as file:
    numbers = file.read().split()

octal_numbers = [num for num in numbers if set(num) <= set("01234567") and int(num, 8) <= max_value_decimal]

for num in octal_numbers:
    words = number_to_words(num)
    print(f"Число: {num} -> {' '.join(words)}")

used_digits = set(''.join(octal_numbers))
used_words = [digit_to_word[digit] for digit in used_digits]

print("\nИспользуемые цифры прописью:")
print(', '.join(used_words))
